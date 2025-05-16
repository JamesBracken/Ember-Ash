from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Booking (models.Model):
    """
    Stores a booking entry to :model:`booking.Booking`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)

    # def __str__(self):
        # return f"Booking for {self.user_id.first_name} on {self.booking_date}"