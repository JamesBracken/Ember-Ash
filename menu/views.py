from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from .forms import MenuForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


def menu(request):
    """
    Renders the main menu page
    """
    return render(request, "menu/menu.html")

# Considered refactoring code of lunch_menu and dinner_menu into one view was 
# however this would actually result in more code so was scrapped
def lunch_menu(request):
    """
    Renders the lunch menu page

    **Context**

    ``menu items``
        All instances of :model:`menu.Menu` where meal_category == `lunch`.

    **Template**

    :template:`menu/menu_lunch.html`
    """
    menu_items = Menu.objects.filter(meal_category="lunch").order_by("id")
    return render(
        request, "menu/menu_lunch.html", {"lunch_menu": menu_items}
    )


def dinner_menu(request):
    """
    Renders the dinner menu page

    **Context**

    ``menu item``
        All instances of :model:`menu.Menu` where meal_category == `dinner`.

    **Template**

    :template:`menu/menu_dinner.html`
    """
    menu_items = Menu.objects.filter(meal_category="dinner").order_by("id")
    return render(
        request, "menu/menu_dinner.html", {"dinner_menu": menu_items}
    )


@staff_member_required
def add_menu_item(request):
    """
    Displays a form for admins to add an instance of :model:`menu.Menu`.

    **Context**

    ``menu_form``
    an instance of :form:`menu.MenuForm`

    **Template**

    :template:`menu/menu_form.html`
    """
    if request.method == "POST":
        menu_form = MenuForm(request.POST, request.FILES)
        if menu_form.is_valid():
            meal_category = menu_form.cleaned_data['meal_category']
            menu_form.save()
            messages.add_message(
                request, messages.SUCCESS, "You have successfully added a menu item"
            )
        # Checks if meal_category selected is lunch or menu and redirects to 
        # the corresponding page
        if(meal_category == "lunch"):
            return redirect("lunch_menu")
        elif(meal_category == "dinner"):
            return redirect("dinner_menu")

    else:
        menu_form = MenuForm()

    return render(
        request,
        "menu/menu_form.html",
        {
            "menu_form": menu_form,
        },
    )


@staff_member_required
def edit_menu_item(request, slug):
    """
    Displays a form for admins to edit an existing instance of :model:`menu.Menu`.

    **Context**

    ``menu_item``
    The selected instance of :model:`menu.Menu`
    ``menu_form``
    an instance of :form:`menu.MenuForm`

    **Template**

    :template:`menu/menu_form.html`
    """
    queryset = Menu.objects.all()
    item = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        menu_form = MenuForm(request.POST, request.FILES, instance=item)
        if menu_form.is_valid():
            meal_category = menu_form.cleaned_data['meal_category']
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
            # Checks if meal_category selected is lunch or dinner and redirects to 
            # the corresponding menu page
        if(meal_category == "lunch"):
            return redirect("lunch_menu")
        elif(meal_category == "dinner"):
            return redirect("dinner_menu")
    else:
        menu_form = MenuForm(instance=item)
    return render(
        request,
        "menu/menu_form.html",
        {
            "menu_form": menu_form,
            "item": item,
        },
    )


@staff_member_required
def delete_menu_item(request, id):
    """
    Deletes an instance of :model:`menu.Menu`.

    **Context**

    ``menu_item``
    The selected instance of :model:`menu.Menu`

    **Template**

    :template:`menu/menu_lunch.html`
    OR
    :template:`menu/menu_dinner.html`
    """
    queryset = Menu.objects.all()
    item = get_object_or_404(queryset, id=id)
    meal_category = item.meal_category
    item.delete()
    messages.add_message(request, messages.SUCCESS, "Menu item has been deleted")
    # Checks if meal_category selected is lunch or dinner and redirects to 
    # the corresponding menu page
    if(meal_category == "lunch"):
        return redirect("lunch_menu")
    elif(meal_category == "dinner"):
        return redirect("dinner_menu")