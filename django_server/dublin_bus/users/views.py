from django.shortcuts import render,redirect
# importing the UserCreation form and modification forms as well
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# for the messages
from django.contrib import messages
#the page restriction library
from django.contrib.auth.decorators import login_required
# leap_card
from .leap_card import get_leap
from .models import Profile
from django.contrib.auth.models import User


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


@login_required
def account(request):
    # instantiating both the forms 
    # user_form = UserUpdateForm(instance=request.user)
    # account_form = ProfileUpdateForm()
    if (request.method == 'POST'):
        user_form = UserUpdateForm(request.POST,instance=request.user)
        account_form = ProfileUpdateForm(request.POST,
            request.FILES,instance=request.user.profile)
        # saving if the post request is valid
        print("user_form.is_valid():",user_form.is_valid())
        print("account_form.is_valid():",account_form.is_valid())
        if (user_form.is_valid() and account_form.is_valid()):

            print("user_form.is_valid():",user_form.is_valid())
            print("account_form.is_valid():",account_form.is_valid())
            print("SAVE INItiATEd")
            # so to get the current user I just get it from requests which seems to work or use form data like in register
            balance = vars(get_leap(request.user.profile.leap_username,request.user.profile.leap_password))

            user_form.save()
            account_form.save()
            x = User.objects.get(username=request.user)
            z=x.profile
            z.leap_balance = balance['balance']
            
            z.save(update_fields =['leap_balance'])   
            # trying vars to get result in a dict
            print(balance["balance"])
            print(request.user)
            messages.success(request, f'Your account has been updated!')
            return redirect('account')
    else:
        # instantiating both the forms
        print("gone to the else case")
        user_form = UserUpdateForm(instance=request.user)
        account_form = ProfileUpdateForm(instance=request.user.profile)
 
    # create a context dictionary to pass both the forms to template
    context ={
        'user_form':user_form,
        'account_form':account_form
    }

    return render(request, 'users/account.html',context)
