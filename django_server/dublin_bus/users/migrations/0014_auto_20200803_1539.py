# Generated by Django 3.0.3 on 2020-08-03 15:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_auto_20200803_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouriteDestinations',
            new_name='FavouriteDestination',
        ),
    ]
