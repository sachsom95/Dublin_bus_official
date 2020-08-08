from django.contrib import admin
from .models import Currentweather, Forecastweather, Covid

# Register your models here.
admin.site.register(Currentweather)
admin.site.register(Forecastweather)
admin.site.register(Covid)
