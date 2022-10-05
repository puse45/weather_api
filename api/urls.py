from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from location.urls import api_urlpatterns as locations_urls

app_name = "api"

router = DefaultRouter()


schema_view = get_swagger_view(title="API Playground")
urlpatterns = [
    path("", include(router.urls)),
    path("playground/", schema_view, name="playground"),
    path("locations/", include(locations_urls)),
]
