from django.shortcuts import render
from .models import Booking
from django.urls import path
from .forms import BookingForm

# Create your views here.

# Creating forms.py then editing this content

def Booking(request):
    # booking = Booking.objects.all()

    booking_form = BookingForm()
    return render(
        request,
        "booking/booking_form.html",
        {"booking_form": booking_form,
         }
    )