"""
Author: Sachin
Inherits the User Registration form and adds 
leap card and email
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# impoting the profile model
from .models import Profile

# leap_card
from .leap_card import get_leap
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# extending from Model form to make custom forms
class UserUpdateForm(forms.ModelForm):
    # since I created a custom field in user I have to create one here as well
    email = forms.EmailField()

    class Meta:
        model = User
        # Username and Email are the ones I will try to modify
        fields = ["username", "email"]


# Form for updating the profile of user I probably should not
# extend from ModelForms but I am too lazy to read docs
class ProfileUpdateForm(forms.ModelForm):
    # to make it a passowrd field still i guess not secure
    leap_password = forms.CharField(
        max_length=32, widget=forms.PasswordInput, required=False
    )
    leap_password_confirm = forms.CharField(
        max_length=32, widget=forms.PasswordInput, required=False
    )

    # Now I need to find a way to confirm if leap credentials are right
    # So as per docs i need to create a class with name class_field_to_check
    def clean_leap_password_confirm(self):
        data1 = self.cleaned_data["leap_password"]
        data2 = self.cleaned_data["leap_password_confirm"]
        username = self.cleaned_data["leap_username"]
        if data1 != data2:
            raise forms.ValidationError("Both field don't match")
        return data1

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get("leap_password_confirm")
        username = self.cleaned_data.get("leap_username")

        if not get_leap(username, password):
            raise forms.ValidationError(
                "Enter Leap-card Credentials to confirm Edit of Account including change of Profile Picture"
            )

    class Meta:
        # May be I should Update leap_card_password in more secure manner?
        model = Profile
        fields = ["image", "leap_username", "leap_password"]
        widgets = {
            "is_registered": forms.HiddenInput(),
            "leap_card_number": forms.HiddenInput(),
            "leap_card_status": forms.HiddenInput(),
            "leap_card_type": forms.HiddenInput(),
            "leap_credit_status": forms.HiddenInput(),
            "leap_expiry_date": forms.HiddenInput(),
            "leap_issue_date": forms.HiddenInput(),
            "leap_auto_topup": forms.HiddenInput(),
            "image": forms.FileInput(),
        }

    field_order = ["leap_username", "leap_password", "leap_password_confirm", "image"]

