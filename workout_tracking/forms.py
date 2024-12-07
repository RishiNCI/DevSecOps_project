# workout_tracking/forms.py
from django import forms
from .models import WorkoutSession, Exercise
from django.forms import inlineformset_factory

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']

ExerciseFormSet = inlineformset_factory(
    WorkoutSession,
    Exercise,
    form=ExerciseForm,
    extra=1,
    can_delete=True
)
