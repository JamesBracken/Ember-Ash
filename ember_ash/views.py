from allauth.account.views import LoginView

# View to connect the custom login modal with allauth
class ModalLogin(LoginView):
    template_name = "base.html"
