import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_bus.settings")

import django
django.setup()

from bus.models import Currentweather

w = Currentweather()

w.dt = 908763

w.dt_iso = '2020-07-15 14:20:19'

w.save()