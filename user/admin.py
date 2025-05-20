from django.contrib import admin
from .models import Customer

# Registers customer models for admins
admin.site.register(Customer)