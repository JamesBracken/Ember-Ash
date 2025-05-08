from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from booking.models import Booking

# Create your views here.

def customer_profile(request):
    user_bookings = Booking.objects.filter(user=request.user)
    # template_name = "user/my_profile.html"
    # Consider using Paginate

    return render(
        request,
        "my_profile.html",
        {
            "bookings": user_bookings,
        }
    )


# def booking_edit():

# def booking_delete():






# def signup(request):


#     if request == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_urls')
#     else:
#             messages.add_message(request, messages.ERROR, "Kindly fill in the form correctly and then submit")