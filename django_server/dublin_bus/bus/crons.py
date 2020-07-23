#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
def currentweather():
    # f=open('/Users/chenpeng/PycharmProjects/comp_47360/Dublin_bus_official/django_server/dublin_bus/bus/test.txt','w')
    # f.writelines('hello')
    # f.close()
    # exec(open("Currentweather_update.py").read())
    os.system("/opt/anaconda3/envs/comp47350py37/bin/python /Users/chenpeng/PycharmProjects/comp_47360/Dublin_bus_official/django_server/dublin_bus/bus/Currentweather_update.py")

def forecastweather():
    os.system("/opt/anaconda3/envs/comp47350py37/bin/python /Users/chenpeng/PycharmProjects/comp_47360/Dublin_bus_official/django_server/dublin_bus/bus/Forecasttweather_update.py")

def covid():
    os.system("/opt/anaconda3/envs/comp47350py37/bin/python /Users/chenpeng/PycharmProjects/comp_47360/Dublin_bus_official/django_server/dublin_bus/bus/Covid_update.py")