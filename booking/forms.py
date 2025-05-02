from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Creates a form for :model:`booking.Booking`
    """
    
    class Meta:
        model = Booking
        fields = ("booking_date", "booking_time", "guests_qty", "comment")