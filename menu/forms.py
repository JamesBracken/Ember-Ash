from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    """
    Creates a form for :model:`menu.Menu`
    """
    class Meta:
        MEAL_CATEGORIES = [("lunch", "Lunch"), ("dinner" ,"Dinner")]
        model = Menu
        fields = ("title", "description", "img", "price", "meal_category",)
        widgets = {
            "meal_category": forms.Select(choices=MEAL_CATEGORIES),
            "title": forms.TextInput(attrs={"maxlength":74}),
            "description": forms.TextInput(attrs={"maxlength":149}),
            "price": forms.TextInput(attrs={"max_digits":6}),
        }