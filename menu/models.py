from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.


class Menu (models.Model):
    id = models.AutoField(unique=True, primary_key=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    slug = models.SlugField(unique=True)
    # Can set default img to placeholder just incase
    img = CloudinaryField('image', default='placeholder')
    price = models.DecimalField()
    meal_category = models.SelectField()

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(str(self.title))
            return super().save(*args, **kwargs)
        super().save(*args, **kwargs)