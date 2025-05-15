from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Booking (models.Model):
    """
    Stores a booking entry to :model:`booking.Booking`.
    """
    # Learned AutoField at https://www.geeksforgeeks.org/how-to-add-an-auto-increment-integer-field-in-django/
    # booking_number = models.AutoField(primary_key=True, unique=True)
    # TEMPORARILY COMMENTING OUT
    slug = models.SlugField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, null=True, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests_qty = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)

# Set slug to booking id (unique)
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(str(self.id))
            return super().save(*args, **kwargs)
        super().save(*args, **kwargs)



    # def __str__(self):
        # return f"Booking for {self.user_id.first_name} on {self.booking_date}"