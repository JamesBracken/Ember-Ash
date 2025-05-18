"""
URL configuration for ember_ash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from .views import ModalLogin
from . import views
# from booking import views as booking_views
from booking.views import trigger_login_message

urlpatterns = [
    path('', views.home, name='home_urls'),
    path('login/', views.login_view, name='login_url'),
    # path('', include('home.urls'), name='home_urls'),
    path('', include('booking.urls'), name='booking_form'),
    path('', include('user.urls'), name='my_profile'),
    path('', include('menu.urls'), name='menu'),
    path('trigger-login-message', trigger_login_message, name='trigger_login_message'),
    # path('accounts/login/', views.ModalLogin.as_view(), name='account_login'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
