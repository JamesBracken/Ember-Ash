from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.booking, name='booking_form'),
    path('booking/<int:id>', views.booking_edit, name='booking_form_edit'),
# 
]