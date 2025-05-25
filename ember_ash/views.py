from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    """
    Renders the home page
    """
    return render(request, 'index.html')


def login_view(request):
    """
    Handles the user login modal, authentication and error handling (ajax)
    """
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "You have successfully logged in"
            )
            return JsonResponse({
                "success": True,
                "home_url": reverse("home_urls")
            })
        else:
            errors = form.errors.as_json()
            return JsonResponse({
                "success": False,
                "errors": errors
            }, status=400)

    return render(request, "index.html", {"login_form": form})
