from django.test import TestCase,Client 
from django.urls import reverse
from  bus.models import Currentweather,Forecastweather,Covid
from  users.models import FavouriteDestination
from django.contrib.auth.models import User
# Create your tests here.

class PostTest(TestCase):

    def setUp(self):
        # user = User.objects.create(username='testuser')
        # user.set_password('12345')
        # user.save()
        self.logged_in_client = Client()
        self.client = Client()
        self.logged_in_client.force_login(User.objects.get_or_create(username='testuser')[0])
        # logged_in = self.client.login(username='testuser', password='12345')
        # self.client = User.objects.create_user(username='sachinsoman', password='123')
        Currentweather.objects.create(dt='1595949928',temp='16',temp_min='15',temp_max='16',pressure='1016',humidity='63',wind_speed='9.3',wind_deg='280',clouds_all='75',weather_id='803',weather_main='Clouds',weather_description='broken_clouds',weather_icon='04d')
        Forecastweather.objects.create(dt='1595949928',temp='16',temp_min='15',temp_max='16',pressure='1016',humidity='63',wind_speed='9.3',wind_deg='280',clouds_all='75',weather_id='803',weather_main='Clouds',weather_description='rain',weather_icon='04d')
        Covid.objects.create(Date='2020-07-23',RequiringICUCovidCases='438',CommunityTransmission='32', TotalConfirmedCovidCases='25826',TotalCovidDeaths='1',ConfirmedCovidCases='1',ConfirmedCovidDeaths='9.3',CloseContact='280',StatisticsProfileDate='75',FID='1',TravelAbroad='1',HospitalisedCovidCases='3')
    def test_tourism_view(self):
        url = reverse('tourism')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        logged_in_response = self.logged_in_client.get(url)
        self.assertEqual(logged_in_response.status_code, 200)

    def test_share_view(self):
        url = reverse(
            "share",
            args={
                "start_lat": 1,
                "start_lng": 1,
                "stop_lat": 1,
                "stop_lng": 1,
                "start": "x",
                "stop": "y",
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_predict_view(self):
        url = reverse('prediction')
        # self.client.post(url, {"line": "46A_12","dep_lat":"1","dep_lng":"1","arr_lat":"1","arr_lng":"1","google_pred":"1"}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        # response = self.client.get(url)
        response = self.client.get(url, {"line": "102","dep_lat":"53.4506925","dep_lng":"-6.1870449999999995","arr_lat":"53.4349011111","arr_lng":"-6.136286666699999","google_pred":"1234"}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_addFavDest_view(self):
        url = reverse('addFavDest')
        response = self.logged_in_client.get(url, {"name": "test","lat":"53.4506925","lng":"-6.1870449999999995"}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)

    def test_delFavDest_view(self):
        url = reverse('delFavDest')
        response = self.logged_in_client.get(url, {"name": "test"}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.status_code, 200)