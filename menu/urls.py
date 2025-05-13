from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/lunch_menu/', views.lunch_menu, name='lunch_menu'),
    # path('menu/lunch_menu/edit_menu_item/<slug:slug>/', views.edit_menu_item, name='lunch_menu_edit'),
    path('menu/dinner_menu/', views.dinner_menu, name='dinner_menu'),
    path('menu/menu_form/', views.add_menu_item, name='add_menu_item'),
    path('menu/menu_form/<slug:slug>', views.edit_menu_item, name='menu_edit'),
]
