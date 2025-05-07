from django.shortcuts import render, redirect
from .models import Booking
from django.urls import path
from .forms import BookingForm

# Create your views here.

# Creating forms.py then editing this content

def booking(request):
    # latest_object = Status.objects.latest('date_added')

    # booking = Booking.objects.all()

    # Defensive design incase object does not exist
    # booking = get_object_or_404(queryset, slug=slug)
    print("updating")

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save(commit=True)
            booking.user = request.user
            # Add messages
            return redirect('home_urls')
    else:
        booking_form = BookingForm()
        
    return render(
        request,
        "booking/booking_form.html",
        {"booking_form": booking_form,
        }
    )


        

