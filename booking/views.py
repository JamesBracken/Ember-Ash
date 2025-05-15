from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import BookingForm
from django.contrib.auth import login_required

# Create your views here.
@login_required
def booking(request):
    """
    Displays a form to create an instance of :model:`booking.Booking`

    **Context**

    ``booking_form``
        An instance of :forms:`booking.BookingForm`
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

@login_required
def booking_edit(request, slug):
    """
    Displays an individual booking for edit.

    **Context**

    ``booking_form``
        An instance of :forms:`booking.BookingForm`
    ``booking``
        An instance of :model:`booking.Booking`
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

@login_required
def booking_delete(request, slug):
    """
    Deletes an individual selected instance of :model:`booking.Booking`

    **Context**

    ``booking``
        An instance of :model:`booking.Booking`
    """
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, slug=slug)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, "Booking was deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own bookings!"
        )

    return HttpResponseRedirect(reverse("my_profile"))


def trigger_login_message(request):
    """
    Displays a message if a user is not authenticated and attempts to make a booking
    """
    messages.add_message(
        request, messages.SUCCESS, "You must login first before making a booking"
    )
    return redirect("home_urls")
