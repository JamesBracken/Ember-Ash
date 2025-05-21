from django.shortcuts import render
from booking.models import Booking
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def customer_profile(request):
    """
    Displays an instance of :model:`user.Customer`
    AND
    Display multiple instances of :model:`booking.Booking`

    **Context**

    `` user_bookings``
        Instances of :model:`booking.Booking`
    """
    user_bookings = Booking.objects.filter(user=request.user).order_by("-booking_date")
    paginator = Paginator(user_bookings, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(
        request,
        "my_profile.html",
        {
            "page_object": page_object,
            "user": request.user,
        }
    )