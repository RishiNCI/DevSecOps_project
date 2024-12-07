# workout_tracking/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_sessions')
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Exercise(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField(help_text="Weight in kg or lbs")

    def __str__(self):
        return f"{self.name} - {self.sets}x{self.reps} @ {self.weight}"
    
class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    duration_weeks = models.IntegerField(default=4)  # Duration in weeks

    def __str__(self):
        return self.name

class Workout(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, related_name="workouts", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    day_of_week = models.IntegerField(choices=[
        (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'),
        (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'),
    ])
    duration_minutes = models.IntegerField(default=60)  # Duration in minutes

    def __str__(self):
        return f"{self.name} on {self.get_day_of_week_display()}"
    
class WorkoutSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.workout.name} on {self.date}"
