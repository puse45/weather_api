from django.urls import path
from rest_framework.routers import DefaultRouter

from location.views import LocationView

app_name = "location"

router = DefaultRouter()
# Register routes

api_urlpatterns = [
    path("<str:city>/", LocationView.as_view(), name="weather_by_city"),
]

urlpatterns = []
