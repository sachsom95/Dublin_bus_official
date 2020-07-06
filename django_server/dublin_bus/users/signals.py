# Author : Sachin
# This file is to create a profile automatically when
# user is created by passing a signal of type post_save

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# so when we get signal from db user creation let the 
# reciver get signal and start the orm query to make 
# the profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


# Signal added to user app.py