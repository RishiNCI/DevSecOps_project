
from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.exercise} on {self.date}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight_goal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calorie_goal = models.PositiveIntegerField(null=True, blank=True)
    workout_goal = models.PositiveIntegerField(help_text="Number of workouts per week", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

class Meal(models.ForeignKey):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=100)  # E.g., breakfast, lunch, snack
    calories = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"
