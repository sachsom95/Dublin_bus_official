#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json

with open(os.path.abspath('static/file_paths.json')) as config_file:
    config = json.load(config_file)

def currentweather():
    # f=open('/Users/chenpeng/PycharmProjects/comp_47360/Dublin_bus_official/django_server/dublin_bus/bus/test.txt','w')
    # f.writelines('hello')
    # f.close()
    # exec(open("Currentweather_update.py").read())
    os.system(config['python_path']+ ' ' + config['current_weather_file'])
    # os.path.abspath('Dublin_bus_official/django_server/dublin_bus/bus/Currentweather_update.py')

def forecastweather():
    os.system(config['python_path']+ ' ' + config['forecast_weather_file'])

def covid():
    os.system(config['python_path']+ ' ' + config['covid_file'])