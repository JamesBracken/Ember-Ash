from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from booking.models import Booking
from booking.forms import BookingForm
from django.http import HttpResponseRedirect


# Create your views here.

def customer_profile(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    # template_name = "user/my_profile.html"
    # Consider using Paginate
    booking_form = BookingForm(data=request.POST)
    return render(
        request,
        "my_profile.html",
        {
            "bookings": user_bookings,
            "booking_form": booking_form,
            "user": request.user,
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
            messages.add_message(request, messages.SUCCESS, 'Booking updated!')
        else:
            messages.add_messages(request, messages.ERROR, 'Error updating booking')
        return HttpResponseRedirect(reverse('my_profile'))


def booking_delete(request, slug, id):
    """
    view to delete a booking
    """
    queryset = booking.objects.all()
    booking = get_object_or_404(queryset, slug=slug)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking was deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own bookings!')

    return HttpResponseRedirect(reverse('my_profile'))


# def signup(request):


#     if request == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_urls')
#     else:
#             messages.add_message(request, messages.ERROR, "Kindly fill in the form correctly and then submit")