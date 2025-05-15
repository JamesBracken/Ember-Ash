from django.urls import path
from . import views
from booking.views import booking_edit, booking_delete
urlpatterns = [
    path('my_profile/', views.customer_profile, name='my_profile'),
    path('edit_booking/<slug:slug>', booking_edit, name='booking_edit'),
    # path('my_profile/edit_booking/<slug:slug>', booking_edit, name='booking_edit'),
    path('my_profile/delete_booking/<slug:slug>', booking_delete, name='booking_delete'),

    # OLD URLS TEMPORARILY LEAVING HERE
    # path('my_profile/delete_booking/<slug:slug>', views.booking_delete, name='booking_delete'),
    # path('my_profile/edit_booking/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    # path('my_profile/', views.customer_profile, name='customer_profile')
]