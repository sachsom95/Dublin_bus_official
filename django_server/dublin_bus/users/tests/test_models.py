from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User


# creating dummy model instances
class ProfileModelTest(TestCase):
    # fixtures = ["users.json", "profiles.json"]

    @classmethod
    def setUp(cls):
        users = User.objects.create(
            username="saurav", password="xyz", email="a@gmail.com"
        )
        z = users
        z.profile.leap_username = "test"
        z.profile.leap_balance = "10"
        z.profile.is_registered = True
        z.profile.leap_card_number = "111"
        z.profile.leap_card_status = "unblocked"
        z.profile.leap_card_type = "student"
        z.profile.leap_credit_status = "True"
        z.profile.leap_expiry_date = "01-01-2019"
        z.profile.leap_issue_date = "01-01-2020"
        z.profile.leap_auto_topup = "Disabled"

    def test_Profile_data(self):
        data = User.objects.get(username="saurav")
        print("<<<<<<<<Verifying Model User Profile>>>>>>")
        self.assertEquals("saurav", str(data))

