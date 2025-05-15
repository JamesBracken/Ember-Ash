from allauth.account.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
# View to connect the custom login modal with allauth




# class ModalLogin(LoginView):
#     template_name = "base.html"

# def trigger_login_message(request):
#     # messages.ERROR(request, "You must login first before making a booking")
#     messages.add_message(request, messages.ERROR, "You must login first before making a booking" )
#     return redirect('home_urls')