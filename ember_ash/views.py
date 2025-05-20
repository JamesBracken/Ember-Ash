from django.shortcuts import render, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    """
    Renders the home page
    """
    return render(request, 'index.html')

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "You have successfully logged in")
            return JsonResponse({"success": True, "home_url": reverse("home_urls") })
        else:
            errors = form.errors.as_json()
            print(errors)
            return JsonResponse({"success": False, "errors": errors}, status=400)

    return render(request, "index.html", {"login_form": form}) 