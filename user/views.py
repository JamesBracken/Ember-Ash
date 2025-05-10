from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from booking.models import Booking
from django.http import HttpResponseRedirect

# Create your views here.

def customer_profile(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    # template_name = "user/my_profile.html"
    # Consider using Paginate

    return render(
        request,
        "my_profile.html",
        {
            "bookings": user_bookings,
        }
    )


def booking_edit(request):
    """
    This view enables editing for bookings
    """
    if request.method == "POST":

        Booking.objects.all()
        booking = get_object_or_404(queryset,)

# def booking_delete():






# def signup(request):


#     if request == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_urls')
#     else:
#             messages.add_message(request, messages.ERROR, "Kindly fill in the form correctly and then submit")