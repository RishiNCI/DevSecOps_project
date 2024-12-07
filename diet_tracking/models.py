# diet_tracking/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField(help_text="Protein in grams")
    carbs = models.FloatField(help_text="Carbohydrates in grams")
    fats = models.FloatField(help_text="Fats in grams")
    water_intake = models.FloatField(help_text="Water intake in liters", default=0.0)

    def __str__(self):
        return f"{self.name} on {self.date}"
    

