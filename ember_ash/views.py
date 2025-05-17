from django.shortcuts import render
# View to connect the custom login modal with allauth




# class ModalLogin(LoginView):
#     template_name = "base.html"

def home(request):
    """
    Renders the home page
    """
    return render(request, 'index.html')