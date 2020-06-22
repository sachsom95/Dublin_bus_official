from django.shortcuts import render
# importing the UserCreation form
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
    