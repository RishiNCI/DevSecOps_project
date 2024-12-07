# diet_tracking/forms.py
from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['date', 'name', 'calories', 'protein', 'carbs', 'fats', 'water_intake']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
