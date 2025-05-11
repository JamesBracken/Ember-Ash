from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm
from django.contrib import messages

# Create your views here.


def menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.all()
    menu_form = MenuForm(data=request.POST)

    return render(request, "menu.html", {"menu_form": menu_form})


def breakfast_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.all()
    menu_form = MenuForm(data=request.POST)

    return render(request, "menu_breakfast.html", {"menu_form": menu_form})


def dinner_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.all()
    menu_form = MenuForm(data=request.POST)

# def edit_menu_item(request):
    """
    Adds a menu item to the menu
    """
    
    # if request.method == "POST":
    #     menu_form = MenuForm(data=request.POST)
    #     if  menu_form.is_valid():
    #         menu_item = menu_form.save()
    #         messages.add_message(
    #             request, messages.SUCCESS, "You have successfully added a menu item"
    #         )
    # else:
    #     menu_form = MenuForm()

# def delete_menu_item