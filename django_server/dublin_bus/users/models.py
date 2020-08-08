from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="default.jpg", upload_to="profile_image", blank=True
    )
    leap_username = models.CharField(max_length=50, default="", blank=True)
    # leap_password = models.CharField(max_length=50, default="", blank=True)
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
