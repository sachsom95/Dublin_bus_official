from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# The profile field will have the


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    leap_username = models.CharField(max_length=50,default='')
    leap_password = models.CharField(max_length=50,default='')
    leap_balance = models.DecimalField(max_digits=4,decimal_places=2, default=0)


    def __str__(self):
        return f'{self.user.username} Profile'