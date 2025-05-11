from . import views
from django.urls import path

urlpatterns = [
    path('my_profile/', views.customer_profile, name='my_profile'),
    # path('edit_booking/<slug:slug>', views.booking_edit, name='booking_edit'),
    path('my_profile/edit_booking/<slug:slug>', views.booking_edit, name='booking_edit'),
    # path('my_profile/edit_booking/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    # path('my_profile/', views.customer_profile, name='customer_profile')
]