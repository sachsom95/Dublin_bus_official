from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'bus/index.html')

def login(request):
    return render(request,'bus/login.html')

def tourism(request):
    return render(request, 'bus/tourism.html')