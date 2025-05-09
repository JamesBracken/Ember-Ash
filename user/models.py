from django.db import models
from booking.models import Booking
from django.contrib.auth.models import User

# Create your models here.

# Not the right naming conventions however I did this on purpose
# to avoid name conflicts with the built in User model in Django
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    want_newsletter = models.BooleanField()
    booking_id = models.ForeignKey(Booking, related_name=('user_booking'), on_delete=models.CASCADE)