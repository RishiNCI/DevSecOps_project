# diet_tracking/admin.py
from django.contrib import admin
from .models import Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'name', 'calories', 'protein', 'carbs', 'fats', 'water_intake')
    list_filter = ('user', 'date')

admin.site.register(Meal, MealAdmin)
