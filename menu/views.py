from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Menu
from .forms import MenuForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


def menu(request):
    """
    Renders the main menu page
    """
    return render(request, "menu.html")

# Refactoring code of lunch_menu and dinner_menu into one view was considered
# however this would actually result in more code so was scrapped
def lunch_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.filter(meal_category="lunch").order_by("id")
    menu_form = MenuForm(data=request.POST)

    return render(
        request, "menu_lunch.html", {"menu_form": menu_form, "lunch_menu": menu_items}
    )


def dinner_menu(request):
    """
    Adds a menu item to the menu
    """
    menu_items = Menu.objects.filter(meal_category="dinner").order_by("id")
    menu_form = MenuForm(data=request.POST)

    return render(
        request, "menu_dinner.html", {"menu_form": menu_form, "dinner_menu": menu_items}
    )


@staff_member_required
def add_menu_item(request):
    """
    Adds a menu item to the menu
    """
    if request.method == "POST":
        menu_form = MenuForm(data=request.POST)
        if menu_form.is_valid():
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


@staff_member_required
def edit_menu_item(request, slug):
    """
    This view edits a menu item
    """
    queryset = Menu.objects.all()
    item = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        menu_form = MenuForm(request.POST, request.FILES, instance=item)
        if menu_form.is_valid():
            menu_form.save()
            messages.add_message(
                request, messages.SUCCESS, "You have successfully edited the menu item"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "An error occurred, the menu item was not updated",
            )
        return HttpResponseRedirect(reverse("menu"))
    else:
        menu_form = MenuForm(instance=item)
    return render(
        request,
        "menu_form.html",
        {
            "menu_form": menu_form,
            "item": item,
        },
    )


@staff_member_required
def delete_menu_item(request, id):
    """
    view to delete a menu item
    """
    queryset = Menu.objects.all()
    item = get_object_or_404(queryset, id=id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, "Menu item has been deleted")
    return redirect("menu")
