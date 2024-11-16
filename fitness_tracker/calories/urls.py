from django.urls import path
from . import views

urlpatterns = [
    path('meal_log/', views.meal_log, name='meal_log'),
]