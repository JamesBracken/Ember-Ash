from django.shortcuts import render
from booking.models import Booking
from booking.forms import BookingForm
from django.core.paginator import Paginator

# Create your views here.

def customer_profile(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    # template_name = "user/my_profile.html"
    # Consider using Paginate
    booking_form = BookingForm(data=request.POST)
    paginator = Paginator(user_bookings, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(
        request,
        "my_profile.html",
        {
            # "bookings": user_bookings,
            "page_object": page_object,
            "booking_form": booking_form,
            "user": request.user,
        }
    )