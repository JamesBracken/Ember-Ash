from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
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


def booking_edit(request, slug):
    """
    This view enables editing for bookings
    """
    if request.method == "POST":
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, slug=slug)
        booking_form = BookingForm(data=request.POST, instance=booking)
        if booking_form.is_valid() and booking.user == request.user:
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Adds a success message
            messages.add_message(request, messages.SUCCESS, "Booking updated!")
        else:
            messages.add_messages(request, messages.ERROR, "Error updating booking")
        return HttpResponseRedirect(reverse("my_profile"))


def booking_delete(request, slug):
    """
    view to delete a booking
    """
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, slug=slug)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, "Booking was deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own bookings!")

    return HttpResponseRedirect(reverse("my_profile"))

def trigger_login_message(request):
    # messages.ERROR(request, "You must login first before making a booking")
    messages.add_message(request, messages.SUCCESS, "You must login first before making a booking" )
    return redirect('home_urls')