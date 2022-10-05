from statistics import median

import requests
from django.conf import settings

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from location.serializers import LocationSerializer


class LocationView(generics.RetrieveAPIView):
    queryset = None
    serializer_class = LocationSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Get weather data for a given city
        @param request days: days -> str : Default = 10
        @param args: None
        @param kwargs: city -> str : Required
        @return: {"maximum":xxx,"minimum":yyy,"average":zzz,"median":aaa}
        """
        serializer = self.serializer_class(
            data=request.GET, context=self.get_serializer_context
        )
        serializer.is_valid(raise_exception=True)
        URL = f"{settings.WEATHER_API_BASE_URL}/v1/forecast.json"
        params = {
            "key": settings.WEATHER_API_KEY,
            "q": kwargs.get("city"),
            "days": serializer.data.get("days"),
        }
        result = requests.get(url=URL, params=params)
        if result.ok:
            data = result.json()
            forecastday = data.get("forecast").get("forecastday")
            maximum, mininum, average, median = get_temp_data(forecastday)
            processed_data = {
                "maximum": maximum,
                "minimum": mininum,
                "average": average,
                "median": median,
            }
            return Response(processed_data, status=status.HTTP_200_OK)
        else:
            return Response(result.json(), status=status.HTTP_400_BAD_REQUEST)


def get_temp_data(forecastday: list) -> tuple:
    """
    Get temperature data from forecastday
    @param forecastday: list
    @return: tuple
    """
    max_temp_list = min_temp_list = avg_temp_list = list()
    for values in forecastday:
        max_temp_list.append(values.get("day").get("maxtemp_c"))
        min_temp_list.append(values.get("day").get("mintemp_c"))
        avg_temp_list.append(values.get("day").get("avgtemp_c"))
    return (
        max(max_temp_list),
        min(min_temp_list),
        round(sum(avg_temp_list) / len(avg_temp_list), 2),
        round(median(avg_temp_list), 2),
    )
