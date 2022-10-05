from django.test import TestCase


class ApiTests(TestCase):
    def test_get_weather_forecast_api(self):
        """
        Test weather api forecast data
        """
        days = 2
        response = self.client.get(f"/api/locations/nairobi/?days={days}")
        self.assertEqual(response.status_code, 200)

    def test_get_weather_forecast_api_more_than_10_days(self):
        """
        To test if days are more than 10
        @return: 400
        """
        days = 12
        response = self.client.get(f"/api/locations/nairobi/?days={days}")
        self.assertEqual(response.status_code, 400)
