from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    Creates the configuration for the booking app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
