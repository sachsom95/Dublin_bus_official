from django.shortcuts import render, redirect

# importing the UserCreation form and modification forms as well
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# for the messages
from django.contrib import messages

# the page restriction library
from django.contrib.auth.decorators import login_required

# leap_card
from .leap_card import get_leap
from .models import Profile
from django.contrib.auth.models import User

# For passing the profile as a python serialized ob
from django.core import serializers

# Cryptography if not found do pip install cryptography
from cryptography.fernet import Fernet


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account made for {username}")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def account(request):
    # instantiating both the forms
    # user_form = UserUpdateForm(instance=request.user)
    # account_form = ProfileUpdateForm()
    if request.method == "POST" and "account" in request.POST:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        account_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        # saving if the post request is valid
        print("user_form.is_valid():", user_form.is_valid())
        print("account_form.is_valid():", account_form.is_valid())
        if user_form.is_valid() and account_form.is_valid():

            print("user_form.is_valid():", user_form.is_valid())
            print("account_form.is_valid():", account_form.is_valid())
            print("SAVE INItiATEd")

            user_form.save()
            # This is commit = False is untill i encrypt password
            commit = account_form.save(commit=False)
            # ---->> ENCRYPTION PROCESS STARTS HERE<<<------
            file = open("key.key", "rb")
            key = file.read()
            file.close()

            encrypted_password = account_form.data["leap_password"].encode()
            f = Fernet(key)
            encrypted_password = f.encrypt(encrypted_password)
            commit.leap_password_binary = encrypted_password
            # ---->> END OF ENCRYPTION BLOCK <<<---------
            commit.save()
            # so to get the current user I just get it from requests which seems to work or use form data like in register
            balance = vars(
                get_leap(
                    request.user.profile.leap_username,
                    f.decrypt(encrypted_password).decode("utf-8"),
                )
            )
            x = User.objects.get(username=request.user)
            z = x.profile
            z.leap_balance = balance["balance"]
            z.is_registered = True
            z.leap_card_number = balance["card_num"]
            z.leap_card_status = balance["card_status"]
            z.leap_card_type = balance["card_type"]
            z.leap_credit_status = balance["credit_status"]
            z.leap_expiry_date = balance["expiry_date"]
            z.leap_issue_date = balance["issue_date"]
            z.leap_auto_topup = balance["auto_topup"]

            z.save(
                update_fields=[
                    "leap_balance",
                    "is_registered",
                    "leap_card_number",
                    "leap_card_status",
                    "leap_card_type",
                    "leap_credit_status",
                    "leap_expiry_date",
                    "leap_issue_date",
                    "leap_auto_topup",
                ]
            )
            # trying vars to get result in a dict
            print(balance["balance"])
            print(request.user)
            messages.success(request, f"Your account has been updated!")
            return redirect("account")
    # the elif is checking which button is pressed whether we pressed the show balance or update buttons
    elif request.method == "POST" and "balance" in request.POST:
        # instantiating both the forms
        print("came to balance")
        # ----->>> DECRYPTION STARTS HERE <<<-------
        file = open("key.key", "rb")
        key = file.read()
        file.close()

        x = User.objects.get(username=request.user)
        z = x.profile
        encrypted_password = z.leap_password_binary
        print("encrypted password:", encrypted_password)
        print(type(encrypted_password))
        # encrypted_password = bytes(encrypted_password, "utf-8")
        # print(type(encrypted_password))

        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password)
        print("decrypted password:", decrypted_password)

        decrypted_password = decrypted_password.decode("utf-8")
        print("decrypted password:", decrypted_password)

        balance = vars(get_leap(request.user.profile.leap_username, decrypted_password))

        z.leap_balance = balance["balance"]

        z.save(update_fields=["leap_balance"])
        # # We any way need to pass an instance of form
        user_form = UserUpdateForm(instance=request.user)
        account_form = ProfileUpdateForm(instance=request.user.profile)

    else:
        # instantiating both the forms
        print("gone to the else case")
        user_form = UserUpdateForm(instance=request.user)
        account_form = ProfileUpdateForm(instance=request.user.profile)
    # create a context dictionary to pass both the forms to template

    context = {
        "user_form": user_form,
        "account_form": account_form,
        "balance": User.objects.get(username=request.user).profile.leap_balance,
        "is_registered": User.objects.get(username=request.user).profile.is_registered,
        # used fileter instead of get as get object not iteratable
        # from stack-overflow  : https://stackoverflow.com/questions/2170228/iterate-over-model-instance-field-names-and-values-in-template
        # Serialization was cool but it kinda put all unnecessary keys as well so back to basics
        # 'profile' : serializers.serialize( "python", Profile.objects.filter(user_id=request.user.id) )
        "profile": Profile.objects.get(user_id=request.user.id),
    }

    return render(request, "users/account.html", context)

