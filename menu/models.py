from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.


class Menu(models.Model):
    """
    Stores a menu item entry
    """
    MEAL_CATEGORIES = [
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    ]
# Delete the below id, its redundant
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    img = CloudinaryField('image', default='cld-sample-4')
    price = models.DecimalField(decimal_places=2, max_digits=6)
    meal_category = models.CharField(choices=MEAL_CATEGORIES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title))
            return super().save(*args, **kwargs)
        super().save(*args, **kwargs)   