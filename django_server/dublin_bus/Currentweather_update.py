#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_bus.settings")
django.setup()

from bus.models import Currentweather

# add api info
apikey = '409a981102cfc744586072ad35c0fb0f'
cityid = '2964574'
url_current = "https://api.openweathermap.org/data/2.5/weather?id=" + cityid + "&APPID=" + apikey

# get json response
response_current = requests.get(url_current)
print("Status code: ", response_current.status_code)
cur_weather = response_current.json()

# delete records in current weather model since we only ever want 1 record
Currentweather.objects.all().delete()

# create an instance of current weather class
w = Currentweather()

# add variables to the instance from openweathermap data
w.dt = cur_weather['dt']
w.temp = cur_weather['main']['temp'] - 273.15
w.temp_min = cur_weather['main']['temp_min']-273.15
w.temp_max = cur_weather['main']['temp_max']-273.15
w.pressure = cur_weather['main']['pressure']
w.humidity = cur_weather['main']['humidity']
w.wind_speed = cur_weather['wind']['speed']
w.wind_deg = cur_weather['wind']['deg']
w.clouds_all = cur_weather['clouds']['all']
w.weather_id = cur_weather['weather'][0]['id']
w.weather_main = cur_weather['weather'][0]['main']
w.weather_description = cur_weather['weather'][0]['description']
w.weather_icon = cur_weather['weather'][0]['icon']

# save new record
w.save()