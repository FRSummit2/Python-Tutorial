from django.urls import path

from . import views

app_name = 'employee'

urlpatterns = [
    path('emp_temp/', views.employee_template, name='details'),
    path('emp_temp_ind/', views.employee_template_ind, name='index'),
    path('get_employee_data_from_user/', views.get_employee_data_from_user, name='get_data'),
    path('update_employee_data_from_user/', views.update_employee_data_from_user, name='update_data'),
]