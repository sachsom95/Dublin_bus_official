import os
import requests
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_bus.settings")

import django
django.setup()

from bus.models import Currentweather

# get current weather from openweathermap api
apikey='409a981102cfc744586072ad35c0fb0f'
cityid='2964574'

url = "https://api.openweathermap.org/data/2.5/weather?id=" + cityid + "&APPID=" + apikey

response = requests.get(url)
cur_weather = json.loads(response.text)

# delete records in current weather model since we only ever want 1 record 
Currentweather.objects.all().delete()

# create an instance of current weather class
w = Currentweather()

# add variables to the instance from openweathermap data
w.dt = cur_weather['dt']
w.temp = cur_weather['main']['temp'] - 273.15
w.wind_speed = cur_weather['wind']['speed']
w.wind_deg = cur_weather['wind']['deg']
w.weather_id = cur_weather['weather'][0]['id']
w.weather_main = cur_weather['weather'][0]['main']
w.weather_description = cur_weather['weather'][0]['description']
w.weather_icon = cur_weather['weather'][0]['icon']

# save new record
w.save()