from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Stacy made this because django made it for me and it doesn't work, thanks django
# # Create your models here.
# class Currentweather(models.Model):
#     dt = models.IntegerField(primary_key=True)
#     dt_iso = models.DateTimeField()
#     city_id = models.IntegerField(blank=True, null=True)
#     city_name = models.CharField(max_length=45, blank=True, null=True)
#     lat = models.CharField(max_length=45, blank=True, null=True)
#     lon = models.CharField(max_length=45, blank=True, null=True)
#     temp = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
#     temp_min = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
#     temp_max = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
#     pressure = models.CharField(max_length=45, blank=True, null=True)
#     humidity = models.CharField(max_length=45, blank=True, null=True)
#     wind_speed = models.CharField(max_length=45, blank=True, null=True)
#     wind_deg = models.CharField(max_length=45, blank=True, null=True)
#     clouds_all = models.IntegerField(blank=True, null=True)
#     weather_id = models.IntegerField(blank=True, null=True)
#     weather_main = models.CharField(max_length=45, blank=True, null=True)
#     weather_description = models.CharField(max_length=45, blank=True, null=True)
#     weather_icon = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'currentWeather'


# The profile field will have the


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="default.jpg", upload_to="profile_image", blank=True
    )
    leap_username = models.CharField(max_length=50, default="", blank=True)
    leap_password = models.CharField(max_length=50, default="", blank=True)
    leap_password_binary = models.BinaryField(max_length=50, default=b"", blank=True)
    leap_balance = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    is_registered = models.BooleanField(default=False)
    leap_card_number = models.CharField(max_length=50, default="", blank=True)
    leap_card_status = models.CharField(max_length=50, default="", blank=True)
    leap_card_type = models.CharField(max_length=50, default="", blank=True)
    leap_credit_status = models.CharField(max_length=50, default="", blank=True)
    leap_expiry_date = models.CharField(max_length=50, default="", blank=True)
    leap_issue_date = models.CharField(max_length=50, default="", blank=True)
    leap_auto_topup = models.CharField(max_length=50, default="", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class FavouriteDestination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    lng = models.DecimalField(max_digits=10, decimal_places=6, default=0)

    def __str__(self):
        return self.user.username + ": " + self.name

    class Meta:
        unique_together = ["user", "name"]
