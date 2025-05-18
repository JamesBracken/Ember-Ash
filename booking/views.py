from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Booking
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
@login_required
def booking(request):
    """
    Displays a form to create an instance of :model:`booking.Booking`

    **Context**

    ``booking_form``
        An instance of :forms:`booking.BookingForm`
    
    **Template**

    ``booking_form.html``
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Adds a success message
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking successfully created, you may view this in your My Profile area",
            )
            return redirect("home_urls")
    else:
        booking_form = BookingForm()
    return render(
        request,
        "booking/booking_form.html",
        {
            "booking_form": booking_form,
        },
    )


# Checks if a specified date is in the future or not
def is_date_in_future(date):
    """
    Checks if a passed in `date` is in the future

    ``Context``

        date passed in as a parameter to check if it is in the future
    """
    today = date.today()
    return date > today


@login_required
def booking_edit(request, id):
    """
    Displays an individual booking for edit.

    **Context**

    ``booking_form``
        An instance of :forms:`booking.BookingForm`
    ``booking``
        An instance of :model:`booking.Booking`
        
    **Template**

    ``booking_form.html``
    """
    
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, id=id)
    booking_form = BookingForm(data=request.POST, instance=booking)
    booking_date = booking.booking_date
    print(booking_date)
    print(is_date_in_future(booking_date))
    if request.method == "POST"  and is_date_in_future(booking_date):
        if booking_form.is_valid() and booking.user == request.user:
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Adds a success message
            messages.add_message(request, messages.SUCCESS, "Booking updated!")
            return redirect("home_urls")
        else:
            messages.add_message(request, messages.ERROR, "Error updating booking")
            return redirect("home_urls")
    else:
        booking_form = BookingForm(instance=booking)
    # return render
    if  is_date_in_future(booking_date):
        return render(
            request,
            "booking/booking_form.html", {
                "booking_form": booking_form,
                "booking_item": booking,
            }
        )
    else: 
        messages.add_message(request, messages.ERROR, "You cannot edit a booking which is in the past")
        return redirect("my_profile")

@login_required
def booking_delete(request, id):
    """
    Deletes an individual selected instance of :model:`booking.Booking`

    **Context**

    ``booking``
        An instance of :model:`booking.Booking`
    """
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, id=id)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, "Booking was deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own bookings!"
        )

    return redirect("home_urls")


def trigger_login_message(request):
    """
    Displays a message if a user is not authenticated and attempts to make a booking
    """
    messages.add_message(
        request, messages.SUCCESS, "You must login first before making a booking"
    )
    return redirect("home_urls")
