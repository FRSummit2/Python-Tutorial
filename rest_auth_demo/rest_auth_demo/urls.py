from django.contrib import admin
from django.urls import path, include
from accounts.views import LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', include('user_auth.urls')),
    # path('', include('accounts.urls')),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
