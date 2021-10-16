from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from . import views

app_name = 'auth_test'

urlpatterns = [
    path('', views.AuthTest.as_view()),
]
