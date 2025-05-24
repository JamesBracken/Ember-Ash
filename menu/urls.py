from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("menu/lunch_menu/", views.lunch_menu, name="lunch_menu"),
    path(
        "menu/lunch_menu/delete_booking/<int:id>",
        views.delete_menu_item,
        name="menu_delete",
    ),
    path("menu/dinner_menu/", views.dinner_menu, name="dinner_menu"),
    path(
        "menu/dinner_menu/delete_booking/<int:id>",
        views.delete_menu_item,
        name="menu_delete",
    ),
    path("menu/menu_form/", views.add_menu_item, name="add_menu_item"),
    path("menu/menu_form/<slug:slug>", views.edit_menu_item, name="menu_edit"),
]
