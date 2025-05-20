from django.db import models
from django.contrib.auth.models import User


class Booking (models.Model):
    """
    Stores a booking entry related to :model:`auth.user`.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)