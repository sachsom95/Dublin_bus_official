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
        return datetime.fromtimestamp(int(self.dt))

    # def __str__(self):
    #     return self.weather_icon
    # class Meta:
    #     db_table = 'currentWeather'
    #     app_label = "dublin_bus"

# class forecastWeather(models.Model):
#     dt = models.CharField(max_length=45,primary_key=True)
#     dt_iso = models.DateField()
#     timestamp = models.DateField()
#     temp = models.CharField(max_length=45)
#     temp_min = models.CharField(max_length=45)
#     temp_max = models.CharField(max_length=45)
#     pressure = models.CharField(max_length=45)
#     humidity = models.CharField(max_length=45)
#     wind_speed = models.CharField(max_length=45)
#     wind_deg = models.CharField(max_length=45)
#     clouds_all = models.CharField(max_length=45)
#     weather_id = models.CharField(max_length=45)
#     weather_main = models.CharField(max_length=45)
#     weather_description = models.CharField(max_length=45)
#     weather_icon = models.CharField(max_length=45)

#     class Meta:
#         db_table = 'forecastWeather'
#         app_label = "dublin_bus"

# class covid(models.Model):
#     Date = models.CharField(max_length=45,primary_key=True)
#     RequiringICUCovidCases = models.CharField(max_length=45)
#     CommunityTransmission = models.CharField(max_length=45)
#     TotalConfirmedCovidCases = models.CharField(max_length=45)
#     TotalCovidDeaths = models.CharField(max_length=45)
#     ConfirmedCovidCases = models.CharField(max_length=45)
#     ConfirmedCovidDeaths = models.CharField(max_length=45)
#     CloseContact = models.CharField(max_length=45)
#     StatisticsProfileDate = models.CharField(max_length=45)
#     FID = models.CharField(max_length=45)
#     TravelAbroad = models.CharField(max_length=45)
#     HospitalisedCovidCases = models.CharField(max_length=45)
#     timestamp = models.DateField()
#     # def __str__(self):
#     #     return self.weather_icon

#     class Meta:
#         db_table = 'covid'
#         app_label = "dublin_bus"

