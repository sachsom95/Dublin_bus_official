from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Currentweather, Forecastweather, Covid

# Create your views here.
def home(request):
    return render(request, 'bus/index.html')

def tourism(request):
    return render(request, 'bus/tourism.html')

def covid_and_weather(request):
    weather = Currentweather.objects.all()[0]
    # print(weather)
    forecast = Forecastweather.objects.all()
    # print(forecast)
    cov_info = Covid.objects.all().order_by('-Date')[0]
    # print(cov_info)
    cov_chart = Covid.objects.all().order_by('Date')
    # print(cov_chart)
    return render(request, 'bus/test.html',{ 'weather_info':weather, 'forecast':forecast, 'covid':cov_info,'covid_chart':cov_chart})

# def covid_chart(request):
#     cov_chart = covid.objects.using('dublin_bus').all().order_by('Date')
#     print(cov_chart)
#     # cov_chart = {'name':123, 'age':123}
#     return JsonResponse(cov_chart)

# def test(request):
#     cov = covid.objects.using('dublin_bus').all().order_by('-Date')
#     print(cov)
#     return render(request,'bus/test.html', {'covid':cov})