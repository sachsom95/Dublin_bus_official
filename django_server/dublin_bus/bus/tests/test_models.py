from django.test import TestCase
from bus.models import Currentweather, Forecastweather, Covid

# creating dummy model instances
class CurrentweatherModelTest(TestCase):
    @classmethod
    def setUp(cls):
        Currentweather.objects.create(
            dt="12-01-2019",
            temp="10",
            temp_min="5",
            temp_max="15",
            pressure="10",
            humidity="5",
            wind_speed="5",
            wind_deg="2",
            clouds_all="1",
            weather_id="test",
            weather_main="test",
            weather_description="rain",
            weather_icon="101",
        )

        Forecastweather.objects.create(
            dt="12-01-2019",
            temp="10",
            temp_min="5",
            temp_max="15",
            pressure="10",
            humidity="5",
            wind_speed="5",
            wind_deg="2",
            clouds_all="1",
            weather_id="test",
            weather_main="test",
            weather_description="rain",
            weather_icon="101",
        )

        Covid.objects.create(
            Date="12-01-2019",
            RequiringICUCovidCases="10",
            CommunityTransmission="5",
            TotalConfirmedCovidCases="15",
            TotalCovidDeaths="10",
            ConfirmedCovidCases="5",
            ConfirmedCovidDeaths="5",
            CloseContact="2",
            StatisticsProfileDate="1",
            FID="test",
            TravelAbroad="10",
            HospitalisedCovidCases="1",
        )

    # this test if model repects the max length restiction on fields

    def test_max_length_CovidModel(self):
        covid = Covid.objects.get(Date="12-01-2019")
        max_length = covid._meta.get_field("Date").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("RequiringICUCovidCases").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("CommunityTransmission").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("TotalConfirmedCovidCases").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("TotalCovidDeaths").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("ConfirmedCovidCases").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("ConfirmedCovidDeaths").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("CloseContact").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("StatisticsProfileDate").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("FID").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("TravelAbroad").max_length
        self.assertEquals(max_length, 45)

        max_length = covid._meta.get_field("HospitalisedCovidCases").max_length
        self.assertEquals(max_length, 45)

    def test_max_length_CurrentweatherModel(self):
        current_weather = Currentweather.objects.get(temp="10")
        max_length = current_weather._meta.get_field("dt").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp_min").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp_max").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("pressure").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("humidity").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("wind_speed").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("wind_deg").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("clouds_all").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_id").max_length
        self.assertEquals(max_length, 45)

    def test_max_length_ForecastweatherModel(self):
        current_weather = Forecastweather.objects.get(temp="10")
        max_length = current_weather._meta.get_field("dt").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp_min").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("temp_max").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("pressure").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("humidity").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("wind_speed").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("wind_deg").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("clouds_all").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_id").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_main").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_description").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_icon").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_main").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_description").max_length
        self.assertEquals(max_length, 45)

        max_length = current_weather._meta.get_field("weather_icon").max_length
        self.assertEquals(max_length, 45)

    def test_Currentweather_data(self):
        data = Currentweather.objects.get(dt="12-01-2019")
        expected_data = (
            f"{data.dt},"
            f"{data.temp},"
            f"{data.temp_min},"
            f"{data.temp_max},"
            f"{data.pressure},"
            f"{data.humidity},"
            f"{data.wind_speed},"
            f"{data.wind_deg},"
            f"{data.clouds_all},"
            f"{data.weather_id},"
            f"{data.weather_main},"
            f"{data.weather_description},"
            f"{data.weather_icon},"
        )
        print("<<<<<<<<Verifying Model Current Weather>>>>>>")
        self.assertEquals(expected_data, str(data))

    def test_Forecastweather_data(self):
        data = Forecastweather.objects.get(dt="12-01-2019")
        expected_data = (
            f"{data.dt},"
            f"{data.dt_iso},"
            f"{data.temp},"
            f"{data.temp_min},"
            f"{data.temp_max},"
            f"{data.pressure},"
            f"{data.humidity},"
            f"{data.wind_speed},"
            f"{data.wind_deg},"
            f"{data.clouds_all},"
            f"{data.weather_id},"
            f"{data.weather_main},"
            f"{data.weather_description},"
            f"{data.weather_icon}"
        )
        print("<<<<<<<<Verifying Model Forcast Weather>>>>>>")
        self.assertEquals(expected_data, str(data))

    def test_Covid_data(self):
        data = Covid.objects.get(Date="12-01-2019")
        expected_data = (
            f"{data.Date},"
            f"{data.RequiringICUCovidCases},"
            f"{data.CommunityTransmission},"
            f"{data.TotalConfirmedCovidCases},"
            f"{data.TotalCovidDeaths},"
            f"{data.ConfirmedCovidCases},"
            f"{data.ConfirmedCovidDeaths},"
            f"{data.CloseContact},"
            f"{data.StatisticsProfileDate},"
            f"{data.FID},"
            f"{data.TravelAbroad},"
            f"{data.HospitalisedCovidCases}"
        )
        print("<<<<<<<<Verifying Covid Model>>>>>>")
        self.assertEquals(expected_data, str(data))

