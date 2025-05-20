from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Booking (models.Model):
    """
    Stores a booking entry related to :model:`auth.user`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)

    def clean(self):
        super().clean()
        next_day = timezone.now().date() + timedelta(days=1)
        if self.booking_date < next_day:
            raise ValidationError({
                "booking_date": f"Booking date must be at least {next_day.strftime("%Y-%m-%d")}"
            })