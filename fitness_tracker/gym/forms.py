from django import forms
from .models import Workout, Meal

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'sets', 'reps', 'weight']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['date', 'meal_type', 'calories', 'description']