from django.conf.urls import url

from .views import api_docs

app_name = "docs"

urlpatterns = [
    url(r"^(?P<path>.*)$", api_docs, name="index"),
]
