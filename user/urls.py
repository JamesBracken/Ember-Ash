from django.urls import path
from . import views
urlpatterns = [
    path('my_profile/', views.customer_profile, name='my_profile'),
]