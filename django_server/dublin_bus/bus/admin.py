from django.contrib import admin
from .models import Currentweather, Forecastweather, Covid

# add permissions to 3 tables Currentweather, Forecastweather, Covid, while users won't be affected
class CovidAdmin(admin.ModelAdmin):
    # forbid add
    def has_add_permission(self, request, obj=None):
        return False
    # forbid change
    def has_change_permission(self, request, obj=None):
        return False
    # forbid delete
    def has_delete_permission(self, request, obj=None):
        return False
class CurrentweatherAdmin(admin.ModelAdmin):
    # forbid add
    def has_add_permission(self, request, obj=None):
        return False
class ForecastweatherAdmin(admin.ModelAdmin):
    # forbid add
    def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(Currentweather,CurrentweatherAdmin)
admin.site.register(Forecastweather,ForecastweatherAdmin)
admin.site.register(Covid,CovidAdmin)

admin.site.site_header = 'Dublin Bus Group 8 Administration'
admin.site.site_title = 'Dublin Bus Group 8 Admin'
admin.site.index_title = 'Dublin Bus Group 8 Admin'

