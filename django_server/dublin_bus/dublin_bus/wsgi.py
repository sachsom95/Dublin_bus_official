"""
WSGI config for dublin_bus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

# add the hellodjango project path into the sys.path
# sys.path.append('<PATH_TO_MY_DJANGO_PROJECT>/hellodjango')

# # add the virtualenv site-packages path to the sys.path
# sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dublin_bus.settings')

application = get_wsgi_application()
