from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages
from django.urls import path
from .forms import BookingForm

# Create your views here.

# Creating forms.py then editing this content

def booking(request):
    # latest_object = Status.objects.latest('date_added')

    # booking = Booking.objects.all()

    # Defensive design incase object does not exist
    # booking = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Add messages
            messages.add_message(
                request, messages.SUCCESS,
                "Booking successfully created, you may view this in your My Profile area"
            )
            return redirect("home_urls")
    else:
        booking_form = BookingForm()
        
    return render(
        request,
        "booking/booking_form.html",
        {"booking_form": booking_form,
        }
    )


        

