from django.db import models
from datetime import datetime

# Create your models here.


class Currentweather(models.Model):
    dt = models.CharField(max_length=45, primary_key=True)
    temp = models.CharField(max_length=45, null=True)
    temp_min = models.CharField(max_length=45, null=True)
    temp_max = models.CharField(max_length=45, null=True)
    pressure = models.CharField(max_length=45, null=True)
    humidity = models.CharField(max_length=45, null=True)
    wind_speed = models.CharField(max_length=45, null=True)
    wind_deg = models.CharField(max_length=45, null=True)
    clouds_all = models.CharField(max_length=45, null=True)
    weather_id = models.CharField(max_length=45, null=True)
    weather_main = models.CharField(max_length=45, null=True)
    weather_description = models.CharField(max_length=45, null=True)
    weather_icon = models.CharField(max_length=45, null=True)

    def __str__(self):
        data = (
            f"{self.dt},"
            f"{self.temp},"
            f"{self.temp_min},"
            f"{self.temp_max},"
            f"{self.pressure},"
            f"{self.humidity},"
            f"{self.wind_speed},"
            f"{self.wind_deg},"
            f"{self.clouds_all},"
            f"{self.weather_id},"
            f"{self.weather_main},"
            f"{self.weather_description},"
            f"{self.weather_icon},"
        )
        return data


class Forecastweather(models.Model):
    dt = models.CharField(max_length=45, primary_key=True)
    dt_iso = models.CharField(max_length=45, null=True)
    temp = models.CharField(max_length=45, null=True)
    temp_min = models.CharField(max_length=45, null=True)
    temp_max = models.CharField(max_length=45, null=True)
    pressure = models.CharField(max_length=45, null=True)
    humidity = models.CharField(max_length=45, null=True)
    wind_speed = models.CharField(max_length=45, null=True)
    wind_deg = models.CharField(max_length=45, null=True)
    clouds_all = models.CharField(max_length=45, null=True)
    weather_id = models.CharField(max_length=45, null=True)
    weather_main = models.CharField(max_length=45, null=True)
    weather_description = models.CharField(max_length=45, null=True)
    weather_icon = models.CharField(max_length=45, null=True)

    def __str__(self):
        data = (
            f"{self.dt},"
            f"{self.dt_iso},"
            f"{self.temp},"
            f"{self.temp_min},"
            f"{self.temp_max},"
            f"{self.pressure},"
            f"{self.humidity},"
            f"{self.wind_speed},"
            f"{self.wind_deg},"
            f"{self.clouds_all},"
            f"{self.weather_id},"
            f"{self.weather_main},"
            f"{self.weather_description},"
            f"{self.weather_icon}"
        )
        return data


class Covid(models.Model):
    Date = models.CharField(max_length=45, primary_key=True)
    RequiringICUCovidCases = models.CharField(max_length=45, null=True)
    CommunityTransmission = models.CharField(max_length=45, null=True)
    TotalConfirmedCovidCases = models.CharField(max_length=45, null=True)
    TotalCovidDeaths = models.CharField(max_length=45, null=True)
    ConfirmedCovidCases = models.CharField(max_length=45, null=True)
    ConfirmedCovidDeaths = models.CharField(max_length=45, null=True)
    CloseContact = models.CharField(max_length=45, null=True)
    StatisticsProfileDate = models.CharField(max_length=45, null=True)
    FID = models.CharField(max_length=45, null=True)
    TravelAbroad = models.CharField(max_length=45, null=True)
    HospitalisedCovidCases = models.CharField(max_length=45, null=True)

    def __str__(self):
        data = (
            f"{self.Date},"
            f"{self.RequiringICUCovidCases},"
            f"{self.CommunityTransmission},"
            f"{self.TotalConfirmedCovidCases},"
            f"{self.TotalCovidDeaths},"
            f"{self.ConfirmedCovidCases},"
            f"{self.ConfirmedCovidDeaths},"
            f"{self.CloseContact},"
            f"{self.StatisticsProfileDate},"
            f"{self.FID},"
            f"{self.TravelAbroad},"
            f"{self.HospitalisedCovidCases}"
        )
        return data
