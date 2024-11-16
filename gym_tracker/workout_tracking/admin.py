# workout_tracking/admin.py
from django.contrib import admin
from .models import WorkoutSession, Exercise

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    inlines = [ExerciseInline]

admin.site.register(WorkoutSession, WorkoutSessionAdmin)
