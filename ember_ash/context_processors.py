from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_form(request):
    return {'login_form': AuthenticationForm()}

def signup_form(request):
    return {'signup_form': UserCreationForm()}