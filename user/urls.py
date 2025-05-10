from . import views
from django.urls import path

urlpatterns = [
    path('my_profile/', views.customer_profile, name='user_urls'),
    # path('edit_booking/<slug:slug>/', views.booking_edit, name='booking_edit'),
    # path('my_profile/', views.customer_profile, name='customer_profile')
]