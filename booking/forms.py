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

        # guest_qty widgets
        self.fields["guests_qty"].widget.attrs["max"] = 100
        self.fields["guests_qty"].widget.attrs["min"] = 1
    class Meta:
        # Taken from https://stackoverflow.com/questions/51164326/how-can-i-add-choices-to-a-timefield-in-a-django-form
        HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 23)]
        model = Booking
        fields = ("booking_date", "booking_time", "guests_qty", "comment")
        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "booking_time": forms.Select(attrs={"type": "time"}, choices=HOUR_CHOICES),
        }
