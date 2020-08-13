# Author Sachin Soman
# Purpose: To test out if all the django URLS work properly and
# redirects to appropriate views
# This test doesn't deal with models so we can use
# Djangos SimpleTestCase class
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# all the views in bus app we test is imported
from users.views import register, account

# No need to test login, logout as they are from django
class TestUrls(SimpleTestCase):
    """Class used for testing URLS"""

    def test_register_url_resolved(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, register)

    def test_account_url_resolved(self):
        url = reverse("account")
        self.assertEqual(resolve(url).func, account)

