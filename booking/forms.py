from django import forms
from .models import Booking
import datetime
class BookingForm(forms.ModelForm):
    """
    Creates a form for :model:`booking.Booking`
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = datetime.date.today()
        self.fields["booking_date"].widget.attrs["min"] = today
    class Meta:
        model = Booking
        fields = ("booking_date", "booking_time", "guests_qty", "comment")
        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
        }
