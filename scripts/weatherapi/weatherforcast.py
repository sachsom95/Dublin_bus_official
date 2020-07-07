#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# This module uses an api request to get a 5-day weather forecast from openweather map. It is scheduled to run
# every 3 hours. It writes this information to the database table forecastWeather by calling the forecast_writer function
# in the module dbconnect.py. The weather forecast is in 3-hour blocks.


import requests
import json
import sys
import databaseforweather
from time import sleep
import logging

# create log file to register errors
logging.basicConfig(filename='weatherforecastApi.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def connecting_method():
    """Creates an instance of class forecast. Sends api key and city id """
    print("forcast weather acquire starts")
    apikey='409a981102cfc744586072ad35c0fb0f'
    cityid='2964574'
    return Forecast(apikey,cityid)

class Forecast:

    def __init__(self, apikey, cityid):
        self.key=apikey
        self.cityid=cityid
        self.dictionary=None

    def api_request(self):
        # sends api request to openweathermap, if successful gets  response with forecast data, turns it into a dictionary and returns it.
        url = "http://api.openweathermap.org/data/2.5/forecast?id=" + self.cityid + "&APPID=" + self.key
        response = requests.get(url)
        print("Status code: ", response.status_code)
#        print("Response: ", response.text)
        self.dictionary = response.json()
        return self.dictionary

    def read_response(self, dictionary):
        # breaks down forecast response dictionary into discrete variables and then writes these to the forecastWeather database
        self.weatherlist = self.dictionary['list']
        # print("List is a: ", type(self.weatherlist))
        # print("length of list is ", len(self.weatherlist))
        databaseforweather.empty_table()
        for i in self.weatherlist:
            self.dt = i['dt']
            self.weather = i['weather']
            self.weather_main = i['weather'][0]['main']
            self.weather_description = i['weather'][0]['description']
            self.weather_icon = i['weather'][0]['icon']
            self.weather_id = i['weather'][0]['id']
            self.main = i['main']
            self.temp = i['main']['temp']-273.15
            self.temp_min = i['main']['temp_min']-273.15
            self.temp_max = i['main']['temp_max']-273.15
            self.pressure = i['main']['pressure']
            self.humidity = i['main']['humidity']
            self.clouds_all = i['clouds']['all']
            self.wind_speed = i['wind']['speed']
            self.wind_degree = i['wind']['deg']
            self.dt_iso = i['dt_txt']
            databaseforweather.forecast_writer(self.dt, self.dt_iso, self.temp, self.temp_min, self.temp_max, self.pressure,
                                self.humidity, self.wind_speed, self.wind_degree, self.clouds_all, self.weather_id, self.weather_main, self.weather_description, self.weather_icon)





    def timer(self):
        """ get forecast from openweather map every 3 hours"""

        while True:
            try:
                sleep(120) # 2 min pause so it won't keep sending repeat requests if error has occurred
                dict = forecast.api_request()
                forecast.read_response(dict)
                sleep(10800)

            except Exception as ex:
                logging.error('error at ' + str(ex))
                print("Error!!!!: ", ex)



if __name__ == '__main__':
    forecast = connecting_method()
    forecast.timer()
