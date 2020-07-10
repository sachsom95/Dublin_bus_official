from django.db import models

# Create your models here.

class currentWeather(models.Model):
    dt = models.CharField(max_length=45,primary_key=True)
    dt_iso = models.DateTimeField(auto_now=True)
    city_id = models.CharField(max_length=45)
    city_name = models.CharField(max_length=45)
    lat = models.CharField(max_length=45)
    lon = models.CharField(max_length=45)
    temp = models.CharField(max_length=45)
    temp_min = models.CharField(max_length=45)
    temp_max = models.CharField(max_length=45)
    pressure = models.CharField(max_length=45)
    humidity = models.CharField(max_length=45)
    wind_speed = models.CharField(max_length=45)
    wind_deg = models.CharField(max_length=45)
    clouds_all = models.CharField(max_length=45)
    weather_id = models.CharField(max_length=45)
    weather_main = models.CharField(max_length=45)
    weather_description = models.CharField(max_length=45)
    weather_icon = models.CharField(max_length=45)

    # def __str__(self):
    #     return self.weather_icon

    class Meta:
        db_table = 'currentWeather'
        app_label = "dublin_bus"

