from django.test import TestCase,Client 
from django.urls import reverse
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from users.leap_card import get_leap
from users.models import Profile,FavouriteDestination



class PostTest(TestCase):

    def setUp(self):
        self.logged_in_client = Client()
        self.client = Client()
        self.logged_in_client.force_login(User.objects.get_or_create(username='testuser',email='test@test.com')[0])

    def test_register_view(self):
        url = reverse('register')
        form_data = {'username': 'test1234567','email':'test@test.com','password1':'Complicatedpassword1234567!','password2':'Complicatedpassword1234567!'}
        response = self.client.post(url,form_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_account_view_account(self):
        url = reverse('account')
        user_form_data = {'csrfmiddlewaretoken': ['NrvFdKJdOIw494JQBQWDD5m0iyj9yO4CZfFZjO2JVobrxot14B0fQkQx9npIXm5z'], 'username': ['testuser'], 'email': ['test@test.com'], 'leap_username': ['StacysLeap'], 'leap_password': ['DublinBus!'], 'leap_password_confirm': ['DublinBus!'], 'image': [''], 'account': ['']}
        # profile_form_data = {'username': 'test1234567','email':'test@test.com','password1':'Complicatedpassword1234567!','password2':'Complicatedpassword1234567!'}
        response = self.logged_in_client.post(url,user_form_data)
        self.assertEqual(response.status_code, 302)
    
    def test_account_view_balance(self):
        url = reverse('account')
        user_form_data = {'csrfmiddlewaretoken': ['NrvFdKJdOIw494JQBQWDD5m0iyj9yO4CZfFZjO2JVobrxot14B0fQkQx9npIXm5z'], 'username': ['testuser'], 'email': ['test@test.com'], 'leap_username': ['StacysLeap'], 'leap_password': ['DublinBus!'], 'leap_password_confirm': ['DublinBus!'], 'image': [''], 'balance': ['']}
        # profile_form_data = {'username': 'test1234567','email':'test@test.com','password1':'Complicatedpassword1234567!','password2':'Complicatedpassword1234567!'}
        response = self.logged_in_client.post(url,user_form_data)
        self.assertEqual(response.status_code, 302)