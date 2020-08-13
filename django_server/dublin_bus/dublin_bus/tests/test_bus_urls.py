# Author Sachin Soman
# Purpose: To test out if all the django URLS work properly and
# redirects to appropriate views
# This test doesn't deal with models so we can use
# Djangos SimpleTestCase class
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# all the views in bus app we test is imported
from bus.views import home, tourism, prediction, addFavDest, delFavDest, share


class TestUrls(SimpleTestCase):
    """Class used for testing URLS"""

    def test_home_url_resolved(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_tourism_url_resolved(self):
        url = reverse("tourism")
        self.assertEqual(resolve(url).func, tourism)

    def test_prediction_url_resolved(self):
        url = reverse("prediction")
        self.assertEqual(resolve(url).func, prediction)

    def test_addFavDest_url_resolved(self):
        url = reverse("addFavDest")
        self.assertEqual(resolve(url).func, addFavDest)

    def test_delFavDest_url_resolved(self):
        url = reverse("delFavDest")
        self.assertEqual(resolve(url).func, delFavDest)

    #    Now the share view was tricky as it has parameters
    #    to test that we need to pass dummy arguments so we do that
    # <start_lat>/<start_lng>/<stop_lat>/<stop_lng>/<start>/<stop>/

    def test_share_url_resolved(self):
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
        print(url)
        self.assertEqual(resolve(url).func, share)