from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# Create your models here.

class Booking (models.Model):
    # Learned AutoField at https://www.geeksforgeeks.org/how-to-add-an-auto-increment-integer-field-in-django/
    # booking_number = models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)
    # def __str__(self):
        # return f"Booking for {self.user_id.first_name} on {self.booking_date}"