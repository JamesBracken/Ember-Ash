from . import views
from django.urls import path

urlpatterns = [
    path('my_profile/', views.customer_profile, name='user_urls'),
    # path('<slug:slug>/edit_booking/<int:booking_id>', views.booking_edit, name='booking_edit'),
    # path('my_profile/', views.customer_profile, name='customer_profile')
]