from django.shortcuts import render,redirect
# importing the UserCreation form
from django.contrib.auth.forms import UserCreationForm
# for the messages
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account made for {username}")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
