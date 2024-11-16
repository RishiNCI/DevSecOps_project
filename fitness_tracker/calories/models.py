from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=100)  # E.g., breakfast, lunch, snack
    calories = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"