#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# This module uses an api request to get the current weather information from openweather map. It is scheduled to run
# every half and hour. It writes this information to the database table currentWeather by calling the weather_writer function in the module dbconnect.py

# Also, we wanted to get weather from user geo-location(from longitude and latitude of user location), but we found if we have too many users using the app,
# it will send tons of requests to openeather api, it will cause refuse connnection.



import requests
import databaseforweather
from time import sleep
import logging

# create log file to register errors
logging.basicConfig(filename='weathercurrentApi.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# "id": 6697759,
# "name": "South Dublin",
# "id": 7778677,
# "name": "Dublin City",
# "id": 2964574,
# "name": "Dublin"
def connecting_method():
    """Creates an instance of class weather. Sends api key and city id """
    print("current weather acquire starts")
    apikey='409a981102cfc744586072ad35c0fb0f'
    cityid='2964574'
    return Weather(apikey,cityid)

class Weather:

    def __init__(self, apikey, cityid):
        self.key=apikey
        self.cityid=cityid
        self.dictionary=None

    def api_request(self):
        # sends api request to openweathermap, if successful it will get response with weather data, turns it into a dictionary and returns it.
        url = "https://api.openweathermap.org/data/2.5/weather?id=" + self.cityid + "&APPID=" + self.key
        # print(url)
        response = requests.get(url)
        print("Status code: ", response.status_code)
        self.dictionary = response.json()
        return self.dictionary


# example for weather json file
# {"coord":{"lon":145.77,"lat":-16.92},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"stations","main":{"temp":300.15,"pressure":1007,"humidity":74,"temp_min":300.15,"temp_max":300.15},"visibility":10000,"wind":{"speed":3.6,"deg":160},"clouds":{"all":40},"dt":1485790200,"sys":{"type":1,"id":8166,"message":0.2064,"country":"AU","sunrise":1485720272,"sunset":1485766550},"id":2172797,"name":"Cairns","cod":200}
    def read_response(self, dictionary):
        # breaks down weather response dictionary into discrete variables and then writes these to the currentWeather database
        self.weather = self.dictionary['weather'][0]
        self.weather_main = self.weather['main']
        self.weather_description = self.weather['description']
        self.weather_id = self.weather['id']
        self.weather_icon = self.weather['icon']
        self.temp = self.dictionary['main']['temp']-273.15
        self.pressure = self.dictionary['main']['pressure']
        self.humidity = self.dictionary['main']['humidity']
        self.temp_min = self.dictionary['main']['temp_min']-273.15
        self.temp_max = self.dictionary['main']['temp_max']-273.15
        self.wind_speed = self.dictionary['wind']['speed']
        self.wind_deg = self.dictionary['wind']['deg']
        self.clouds_all = self.dictionary['clouds']['all']
        self.dt = self.dictionary['dt']
        self.city_id = self.dictionary['id']
        self.city_name = self.dictionary['name']
        self.lat = self.dictionary['coord']['lat']
        self.lon = self.dictionary['coord']['lon']
        # print("city id", self.city_id)
        # print("weather description ", self.weather_description)
        databaseforweather.weather_writer(self.dt, self.city_id, self.city_name, self.lat, self.lon, self.temp, self.temp_min, self.temp_max, self.pressure,
                                 self.humidity, self.wind_speed, self.wind_deg, self.clouds_all, self.weather_id, self.weather_main, self.weather_description, self.weather_icon)

    def timer(self):
        """ get weather data from openweather map at 30 min intervals"""
        while True:
            try:
                sleep(120) # 2 min pause so it won't keep sending repeat requests if error has occurred
                dict = weather.api_request()
                weather.read_response(dict)
                sleep(1800)

            except Exception as ex:
                logging.error('error at ' + str(ex))
                print("Request error: ", ex)


weather = connecting_method()
weather.timer()
