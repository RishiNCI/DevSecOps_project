from django.utils.timezone import datetime
from django.shortcuts import render
from .models import Workout
from django.contrib.auth.decorators import login_required
import random
from django.utils import timezone
from datetime import timedelta



SUGGESTED_EXERCISES = ["Push-Ups", "Squats", "Deadlifts", "Bench Press"]
SUGGESTED_MEALS = ["Grilled Chicken Salad", "Oatmeal with Fruit", "Greek Yogurt", "Protein Smoothie"]

@login_required
def workout_log(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    dates = [workout.date for workout in workouts]
    weights = [workout.weight for workout in workouts]
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    # Existing code...
    suggested_exercise = random.choice(SUGGESTED_EXERCISES)
    suggested_meal = random.choice(SUGGESTED_MEALS)

    return render(request, 'gym/workout_log.html', {
        'workouts': workouts,
        'dates': dates,
        'weights': weights,
        'suggested_exercise': suggested_exercise,
        'suggested_meal': suggested_meal,
    })

def summary(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    weekly_workouts = Workout.objects.filter(user=request.user, date__gte=start_of_week)
    weekly_calories = Meal.objects.filter(user=request.user, date__gte=start_of_week)
    total_calories = sum(meal.calories for meal in weekly_calories)
    total_workouts = weekly_workouts.count()

    return render(request, 'gym/summary.html', {
        'total_calories': total_calories,
        'total_workouts': total_workouts,
    })  

@login_required
def dashboard(request):
    profile = request.user.profile
    recent_workouts = Workout.objects.filter(user=request.user).order_by('-date')[:5]
    recent_meals = Meal.objects.filter(user=request.user).order_by('-date')[:5]

    return render(request, 'gym/dashboard.html', {
        'profile': profile,
        'recent_workouts': recent_workouts,
        'recent_meals': recent_meals,
    })