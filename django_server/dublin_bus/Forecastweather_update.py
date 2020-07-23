#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_bus.settings")
django.setup()

from bus.models import Forecastweather

# add api info
apikey = '409a981102cfc744586072ad35c0fb0f'
cityid = '2964574'
url_forecast = "http://api.openweathermap.org/data/2.5/forecast?id=" + cityid + "&APPID=" + apikey

# get json response
response_forecast = requests.get(url_forecast)
print("Status code: ", response_forecast.status_code)
fore_weather = response_forecast.json()
weatherlist = fore_weather['list']

# delete records in forecast weather model since we only ever want new records
Forecastweather.objects.all().delete()

for i in weatherlist:
    w = Forecastweather()
    w.dt = i['dt']
    w.dt_iso = i['dt_txt']
    w.temp = i['main']['temp'] - 273.15
    w.temp_min = i['main']['temp_min'] - 273.15
    w.temp_max = i['main']['temp_max'] - 273.15
    w.pressure = i['main']['pressure']
    w.humidity = i['main']['humidity']
    w.wind_speed = i['wind']['speed']
    w.wind_degree = i['wind']['deg']
    w.clouds_all = i['clouds']['all']
    w.weather_id = i['weather'][0]['id']
    w.weather_main = i['weather'][0]['main']
    w.weather_description = i['weather'][0]['description']
    w.weather_icon = i['weather'][0]['icon']
    w.save()








