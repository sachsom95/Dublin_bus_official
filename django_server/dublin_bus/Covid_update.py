#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import os
import django
import pandas

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_bus.settings")
django.setup()

from bus.models import Covid

# add api info
url_covid = "https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/CovidStatisticsProfileHPSCIrelandOpenData/FeatureServer/0/query?where=1%3D1&outFields=Date,RequiringICUCovidCases,CommunityTransmission,TotalConfirmedCovidCases,TotalCovidDeaths,ConfirmedCovidCases,ConfirmedCovidDeaths,CloseContact,StatisticsProfileDate,FID,TravelAbroad,HospitalisedCovidCases&outSR=4326&f=json"

# get json response
response_covid = requests.get(url_covid)
print("Status code: ", response_covid.status_code)
covid = response_covid.json()
featurelist = covid['features']

# delete records anyway
Covid.objects.all().delete()

# loop and create instance

for i in featurelist:
    # create an instace for ecery loop
    c = Covid()
    attribute = i["attributes"]
    d = attribute["Date"]
    c.Date = (str(pandas.to_datetime(d, unit='ms')))[:10]
    c.RequiringICUCovidCases = attribute["RequiringICUCovidCases"]
    c.CommunityTransmission = attribute["CommunityTransmission"]
    c.TotalConfirmedCovidCases = attribute["TotalConfirmedCovidCases"]
    c.TotalCovidDeaths = attribute["TotalCovidDeaths"]
    c.ConfirmedCovidCases = attribute["ConfirmedCovidCases"]
    c.ConfirmedCovidDeaths = attribute["ConfirmedCovidDeaths"]
    c.CloseContact = attribute["CloseContact"]
    c.StatisticsProfileDate = attribute["StatisticsProfileDate"]
    c.FID = attribute["FID"]
    c.TravelAbroad = attribute["TravelAbroad"]
    c.HospitalisedCovidCases = attribute["HospitalisedCovidCases"]
    c.save()