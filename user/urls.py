from django.urls import path
from . import views
from booking.views import booking_edit, booking_delete
urlpatterns = [
    path('my_profile/', views.customer_profile, name='my_profile'),
]