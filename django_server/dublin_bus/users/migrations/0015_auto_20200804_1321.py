# Generated by Django 3.0.3 on 2020-08-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200803_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritedestination',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
    ]