from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Menu
from .forms import MenuForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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

@login_required
def edit_menu_item(request, slug):
    """
    This view edits a menu item
    """
    queryset = Menu.objects.filter(meal_category="lunch")
    item = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        menu_form = MenuForm(request.POST, instance=item)
        if menu_form.is_valid() and request.user.is_staff:
            menu_item = menu_form.save()
            # Add user feedback in messages
            messages.add_message(request, messages.SUCCESS, "You have successfully edited the menu item")
        else:
            messages.add_message(request, messages.ERROR, "An error occurred, the menu item was not updated")
        return HttpResponseRedirect(reverse("menu"))
    else:
        menu_form = MenuForm(instance=item)
    # return render(request, reverse("lunch_menu_edit"), kwargs={"slug":slug}, 
    return render(request, "menu_form.html", {"menu_form": menu_form, "item":item,} 
                #   {"form": menu_form, "item":item,} {"slug":slug},
                )
# def delete_menu_item