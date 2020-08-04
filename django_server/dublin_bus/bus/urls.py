"""dublin_bus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# importing bus apps view into bus url.py
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('tourism/', views.tourism, name="tourism"),
    path('prediction/', views.prediction, name="prediction"),
    path('share/<start_lat>/<start_lng>/<stop_lat>/<stop_lng>/<start>/<stop>/', views.share, name="share"),
    path('add_fav_destination/', views.addFavDest, name="addFavDest"),
]

# Patch notes:sachin
# removed the login path by stacy as we shift it to user app