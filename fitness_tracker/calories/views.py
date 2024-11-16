from django.shortcuts import render
from .models import Meal
from django.contrib.auth.decorators import login_required

@login_required
def meal_log(request):
    if request.method == "POST":
        # Process the meal logging form
        pass  # Add form handling here
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    return render(request, 'calories/meal_log.html', {'meals': meals})


