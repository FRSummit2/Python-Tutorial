from django.urls import path
from . import views

app_name = 'SD_DELIVERY_PLAN'

urlpatterns = [
    path('', views.DeliveryPlanController.as_view()),
    path('frs-json-data/', views.get_external_api_data, name='get_external_api_data')
]
