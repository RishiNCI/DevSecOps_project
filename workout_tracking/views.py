# workout_tracking/views.py
from django.shortcuts import render, get_object_or_404, redirect, get_object_or_404
from .models import WorkoutSession
from .forms import WorkoutSessionForm, ExerciseFormSet
from django.contrib.auth.decorators import login_required
from .models import WorkoutPlan
from .models import WorkoutSchedule
from datetime import datetime, timedelta



@login_required
def workout_list(request):
    workouts = WorkoutSession.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workout_tracking/workout_list.html', {'workouts': workouts})

@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(WorkoutSession, pk=pk, user=request.user)
    exercises = workout.exercises.all()
    return render(request, 'workout_tracking/workout_detail.html', {'workout': workout, 'exercises': exercises})

@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST)
        formset = ExerciseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            formset.instance = workout
            formset.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutSessionForm()
        formset = ExerciseFormSet()
    return render(request, 'workout_tracking/workout_form.html', {'form': form, 'formset': formset})

@login_required
def workout_edit(request, pk):
    workout = get_object_or_404(WorkoutSession, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, instance=workout)
        formset = ExerciseFormSet(request.POST, instance=workout)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutSessionForm(instance=workout)
        formset = ExerciseFormSet(instance=workout)
    return render(request, 'workout_tracking/workout_form.html', {'form': form, 'formset': formset})

@login_required
def workout_delete(request, pk):
    workout = get_object_or_404(WorkoutSession, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'workout_tracking/workout_confirm_delete.html', {'workout': workout})

def workout_plan_list(request):
    plans = WorkoutPlan.objects.filter(created_by=request.user)
    return render(request, 'workout_tracking/workout_plan_list.html', {'plans': plans})

def workout_plan_detail(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk, created_by=request.user)
    workouts = plan.workouts.all()
    return render(request, 'workout_tracking/workout_plan_detail.html', {'plan': plan, 'workouts': workouts})


def workout_calendar(request):
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    dates = [start_of_week + timedelta(days=i) for i in range(7)]
    workouts = WorkoutSchedule.objects.filter(user=request.user, date__range=[start_of_week, start_of_week + timedelta(days=6)])
    
    # Group workouts by day
    workout_by_day = {date: [] for date in dates}
    for workout in workouts:
        workout_by_day[workout.date].append(workout)
    
    return render(request, 'workout_tracking/workout_calendar.html', {'dates': dates, 'workout_by_day': workout_by_day})