from django.shortcuts import render
from django.http import HttpResponse
from .models import currentWeather

# Create your views here.
def home(request):
    return render(request, 'bus/index.html')

def tourism(request):
    return render(request, 'bus/tourism.html')

def test(request):
    all = currentWeather.objects.using('dublin_bus').all()
    print(all)
    return render(request, 'bus/test.html',{ 'weather_info':all })