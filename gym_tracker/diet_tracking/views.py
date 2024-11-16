# diet_tracking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal
from .forms import MealForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime, timedelta

@login_required
def diet_list(request):
    today = datetime.today()
    meals = Meal.objects.filter(user=request.user, date__lte=today).order_by('-date')
    return render(request, 'diet_tracking/diet_list.html', {'meals': meals})

@login_required
def diet_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk, user=request.user)
    return render(request, 'diet_tracking/diet_detail.html', {'meal': meal})

@login_required
def diet_create(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('diet_detail', pk=meal.pk)
    else:
        form = MealForm()
    return render(request, 'diet_tracking/diet_form.html', {'form': form})

@login_required
def diet_edit(request, pk):
    meal = get_object_or_404(Meal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('diet_detail', pk=meal.pk)
    else:
        form = MealForm(instance=meal)
    return render(request, 'diet_tracking/diet_form.html', {'form': form})

@login_required
def diet_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk, user=request.user)
    if request.method == 'POST':
        meal.delete()
        return redirect('diet_list')
    return render(request, 'diet_tracking/diet_confirm_delete.html', {'meal': meal})

@login_required
def diet_summary(request):
    today = datetime.today().date()
    week_ago = today - timedelta(days=7)
    meals = Meal.objects.filter(user=request.user, date__range=(week_ago, today))
    summary = meals.aggregate(
        total_calories=Sum('calories'),
        total_protein=Sum('protein'),
        total_carbs=Sum('carbs'),
        total_fats=Sum('fats'),
        total_water=Sum('water_intake'),
    )
    return render(request, 'diet_tracking/diet_summary.html', {'summary': summary})
