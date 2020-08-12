from django.test import TestCase,Client 
from django.urls import reverse
from  bus.models import Currentweather,Covid
from django.contrib.auth.models import User
# Create your tests here.

class PostTest(TestCase):

    def setUp(self):
        self.client = Client()
        # self.client = User.objects.create_user(username='sachinsoman', password='123')
        Currentweather.objects.create(dt='1595949928',temp='16',temp_min='15',temp_max='16',pressure='1016',humidity='63',wind_speed='9.3',wind_deg='280',clouds_all='75',weather_id='803',weather_main='Clouds',weather_description='broken_clouds',weather_icon='04d')
        Covid.objects.create(Date='2020-07-23',RequiringICUCovidCases='438',CommunityTransmission='32', TotalConfirmedCovidCases='25826',TotalCovidDeaths='1',ConfirmedCovidCases='1',ConfirmedCovidDeaths='9.3',CloseContact='280',StatisticsProfileDate='75',FID='1',TravelAbroad='1',HospitalisedCovidCases='3')

    def test_tourism_view(self):
        url = reverse('tourism')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)