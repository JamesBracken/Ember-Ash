from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/breakfast_menu/', views.breakfast_menu, name='breakfast_menu'),
    path('menu/dinner_menu/', views.dinner_menu, name='dinner_menu'),
]
