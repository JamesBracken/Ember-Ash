from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    """
    Makes the login_form globally available across the project
    """
    return {'login_form': AuthenticationForm()}