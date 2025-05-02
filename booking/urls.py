from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.Booking, name='booking_form')
]