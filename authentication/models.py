from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings



class CustomUser(AbstractUser):
    # Add additional fields if needed
    pass

from django.contrib.auth.models import User
class UserProfile(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('maintenance', 'Maintenance'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL here
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='maintenance')

    def __str__(self):
        return self.user.username

    def calculate_bmi(self):
        if self.weight and self.height:
            return self.weight / (self.height ** 2)
        return None

    def get_diet_suggestion(self):
        if self.goal == 'weight_loss':
            return "For weight loss, focus on a calorie deficit. Include high-protein, low-carb meals."
        elif self.goal == 'weight_gain':
            return "For weight gain, increase your calorie intake. Focus on healthy fats and protein."
        else:
            return "For maintenance, maintain a balanced diet with sufficient calories for your activity level."