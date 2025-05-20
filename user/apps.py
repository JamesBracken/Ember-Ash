from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Creates the configuration for the user app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'