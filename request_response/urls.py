from django.conf.urls import url
from django.urls import path, re_path

from request_response import views

urlpatterns = [
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather1),
]
