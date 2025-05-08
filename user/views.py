from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


# def signup(request):


#     if request == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_urls')
#     else:
#             messages.add_message(request, messages.ERROR, "Kindly fill in the form correctly and then submit")