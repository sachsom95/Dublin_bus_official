from django.db import models

# Create your models here.

# Create your models here.
class Currentweather(models.Model):
    dt = models.IntegerField(primary_key=True)
    dt_iso = models.DateTimeField()
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=45, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    lon = models.CharField(max_length=45, blank=True, null=True)
    temp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    temp_min = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    temp_max = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    pressure = models.CharField(max_length=45, blank=True, null=True)
    humidity = models.CharField(max_length=45, blank=True, null=True)
    wind_speed = models.CharField(max_length=45, blank=True, null=True)
    wind_deg = models.CharField(max_length=45, blank=True, null=True)
    clouds_all = models.IntegerField(blank=True, null=True)
    weather_id = models.IntegerField(blank=True, null=True)
    weather_main = models.CharField(max_length=45, blank=True, null=True)
    weather_description = models.CharField(max_length=45, blank=True, null=True)
    weather_icon = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currentWeather'