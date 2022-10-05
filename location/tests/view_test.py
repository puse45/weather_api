from unittest.mock import patch
from django.test import TestCase


class TestLocationView(TestCase):
    def setUp(self) -> None:
        self.url = "/api/locations/nairobi/"

    @patch("location.views.get_temp_data")
    def test_location_view(self, mock_get_temp_data):
        """
        Test weather api forecast data
        """
        mock_get_temp_data.return_value = (1, 2, 3, 4)
        response = self.client.get(self.url)
        self.assertEqual(mock_get_temp_data.call_count, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), {"maximum": 1, "minimum": 2, "average": 3, "median": 4}
        )
