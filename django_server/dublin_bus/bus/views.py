from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# from ml_models import *
import os
from django.conf import settings
import pickle
# from django.views.decorators.csrf import csrf_exempt,csrf_protect

with open('/Users/Ben/Desktop/summer_project/Dublin_bus_official/django_server/dublin_bus/bus/static/1_37_grad_boost_model.sav', 'rb') as f:
    model = pickle.load(f)

# Create your views here.
def home(request):
    return render(request, 'bus/index.html')

def login(request):
    return render(request,'bus/login.html')

def tourism(request):
    return render(request, 'bus/tourism.html')

# @csrf_exempt
def prediction(request):
    value = model.predict([[84600.0,5.44,7.20,2924.0,1,0,0,0,0,0,0,0,0,0,0,1]])
    test = []
    for key,value in request.GET.items():
        test.append(value)
    return JsonResponse({'response': test})
