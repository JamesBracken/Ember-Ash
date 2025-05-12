from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    """
    Creates a form for :model:`menu.Menu`
    """
    class Meta:
        MEAL_CATEGORIES = ["Lunch", "Dinner"]
        model = Menu
        fields = ("title", "description", "img", "price", "meal_category",)
        widgets = {
            "meal_category": forms.Select(choices=MEAL_CATEGORIES)
        }