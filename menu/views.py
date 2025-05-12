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


def lunch_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.filter(meal_category="lunch")
    menu_form = MenuForm(data=request.POST)

    return render(request, "menu_lunch.html", {"menu_form": menu_form, "lunch_menu": menu_items})


def dinner_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.all()
    menu_form = MenuForm(data=request.POST)

    return render(request, "menu_dinner.html", {"menu_form": menu_form})


def add_menu_item(request):
    """
    Adds a menu item to the menu
    """
    
    if request.method == "POST":
        menu_form = MenuForm(data=request.POST)
        if menu_form.is_valid and request.user.is_authenticated and request.user.is_staff == True:
            menu_form.save()
            messages.add_message(
                request, messages.SUCCESS, "You have successfully added a menu item"
            )
            return redirect("menu")
    else:
        menu_form = MenuForm()

    return render(
        request,
        "menu_form.html",
        {
            "menu_form": menu_form,
        },
    )


# def delete_menu_item
