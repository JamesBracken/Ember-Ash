from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm


def login_form(request):
    return {'login_form': LoginForm()}

def signup_form(request):
    return {'signup_form': SignupForm()}