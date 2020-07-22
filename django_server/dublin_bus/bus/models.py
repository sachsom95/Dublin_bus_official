from django.db import models
from datetime import datetime 

# Create your models here.

class Currentweather(models.Model):
    dt = models.CharField(max_length=45)
    temp = models.CharField(max_length=45,null=True)
    wind_speed = models.CharField(max_length=45,null=True)
    wind_deg = models.CharField(max_length=45,null=True)
    weather_id = models.CharField(max_length=45,null=True)
    weather_main = models.CharField(max_length=45,null=True)
    weather_description = models.CharField(max_length=45,null=True)
    weather_icon = models.CharField(max_length=45,null=True)
    def __str__(self):
        return str(datetime.fromtimestamp(int(self.dt)))

    # def __str__(self):
    #     return self.weather_icon
    # class Meta:
    #     db_table = 'currentWeather'
    #     app_label = "dublin_bus"

class Forecastweather(models.Model):
    dt = models.CharField(max_length=45)
    temp = models.CharField(max_length=45,null=True)
    wind_speed = models.CharField(max_length=45,null=True)
    wind_deg = models.CharField(max_length=45,null=True)
    weather_id = models.CharField(max_length=45,null=True)
    weather_main = models.CharField(max_length=45,null=True)
    weather_description = models.CharField(max_length=45,null=True)
    weather_icon = models.CharField(max_length=45,null=True)
    def __str__(self):
        return str(datetime.fromtimestamp(int(self.dt)))

#     class Meta:
#         db_table = 'forecastWeather'
#         app_label = "dublin_bus"

class Covid(models.Model):
    Date = models.CharField(max_length=45,primary_key=True)
    RequiringICUCovidCases = models.CharField(max_length=45)
    CommunityTransmission = models.CharField(max_length=45)
    TotalConfirmedCovidCases = models.CharField(max_length=45)
    TotalCovidDeaths = models.CharField(max_length=45)
    ConfirmedCovidCases = models.CharField(max_length=45)
    ConfirmedCovidDeaths = models.CharField(max_length=45)
    CloseContact = models.CharField(max_length=45)
    StatisticsProfileDate = models.CharField(max_length=45)
    FID = models.CharField(max_length=45)
    TravelAbroad = models.CharField(max_length=45)
    HospitalisedCovidCases = models.CharField(max_length=45)
    timestamp = models.DateField()


#     class Meta:
#         db_table = 'covid'
#         app_label = "dublin_bus"

