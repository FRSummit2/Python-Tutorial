"""api_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.EmployeeList.as_view()),
    # path('get_employee_list/', views.get_employee_list, name='get_employee_list'),
    path('employees/list/', views.get_employee_list, name='get_employee_list'),
    path('', include('employee.urls')),
    path('', include('blogs.urls')),
    path('api/sd-delivery-plan/', include('SD_DELIVERY_PLAN.urls')),
    path('api/auth-test/', include('auth_test.urls')),
]
