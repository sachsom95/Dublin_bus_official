from django.shortcuts import render,redirect
# importing the UserCreation form
from .forms import UserRegisterForm
# for the messages
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account made for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def account(request):
    return render(request, 'users/account.html')
