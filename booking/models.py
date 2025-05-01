from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    booking_number = models.IntegerField(unique=True)
    # user_id = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)