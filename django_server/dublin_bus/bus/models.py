from django.db import models
from datetime import datetime 

# Create your models here.

class Currentweather(models.Model):
    dt = models.CharField(max_length=45,primary_key=True)
    temp = models.CharField(max_length=45,null=True)
    temp_min = models.CharField(max_length=45,null=True)
    temp_max = models.CharField(max_length=45,null=True)
    pressure = models.CharField(max_length=45,null=True)
    humidity = models.CharField(max_length=45,null=True)
    wind_speed = models.CharField(max_length=45,null=True)
    wind_deg = models.CharField(max_length=45,null=True)
    clouds_all = models.CharField(max_length=45,null=True)
    weather_id = models.CharField(max_length=45,null=True)
    weather_main = models.CharField(max_length=45,null=True)
    weather_description = models.CharField(max_length=45,null=True)
    weather_icon = models.CharField(max_length=45,null=True)

    def __str__(self):
        return str(datetime.fromtimestamp(int(self.dt)))

class Forecastweather(models.Model):
    dt = models.CharField(max_length=45,primary_key=True)
    dt_iso = models.CharField(max_length=45,null=True)
    temp = models.CharField(max_length=45,null=True)
    temp_min = models.CharField(max_length=45,null=True)
    temp_max = models.CharField(max_length=45,null=True)
    pressure = models.CharField(max_length=45,null=True)
    humidity = models.CharField(max_length=45,null=True)
    wind_speed = models.CharField(max_length=45,null=True)
    wind_deg = models.CharField(max_length=45,null=True)
    clouds_all = models.CharField(max_length=45,null=True)
    weather_id = models.CharField(max_length=45,null=True)
    weather_main = models.CharField(max_length=45,null=True)
    weather_description = models.CharField(max_length=45,null=True)
    weather_icon = models.CharField(max_length=45,null=True)

    def __str__(self):
        return str(self.dt_iso)

class Covid(models.Model):
    Date = models.CharField(max_length=45,primary_key=True)
    RequiringICUCovidCases = models.CharField(max_length=45,null=True)
    CommunityTransmission = models.CharField(max_length=45,null=True)
    TotalConfirmedCovidCases = models.CharField(max_length=45,null=True)
    TotalCovidDeaths = models.CharField(max_length=45,null=True)
    ConfirmedCovidCases = models.CharField(max_length=45,null=True)
    ConfirmedCovidDeaths = models.CharField(max_length=45,null=True)
    CloseContact = models.CharField(max_length=45,null=True)
    StatisticsProfileDate = models.CharField(max_length=45,null=True)
    FID = models.CharField(max_length=45,null=True)
    TravelAbroad = models.CharField(max_length=45,null=True)
    HospitalisedCovidCases = models.CharField(max_length=45,null=True)