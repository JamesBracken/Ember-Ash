from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    """
    Stores a menu item entry
    """
    MEAL_CATEGORIES = [
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    ]
    title = models.CharField(max_length=75, unique=True)
    description = models.TextField(max_length=150)
    slug = models.SlugField(unique=True, max_length=75)
    img = CloudinaryField('image', default='cld-sample-4')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    meal_category = models.CharField(choices=MEAL_CATEGORIES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title))
            return super().save(*args, **kwargs)
        super().save(*args, **kwargs)