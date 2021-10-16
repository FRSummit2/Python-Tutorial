from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.hello2, name='hello2'),
    path('api', views.api, name='api'),
]