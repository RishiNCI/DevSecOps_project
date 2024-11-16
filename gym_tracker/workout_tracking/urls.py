# workout_tracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('create/', views.workout_create, name='workout_create'),
    path('<int:pk>/', views.workout_detail, name='workout_detail'),
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    path('plans/', views.workout_plan_list, name='workout_plan_list'),
    path('plans/<int:pk>/', views.workout_plan_detail, name='workout_plan_detail'),
    path('calendar/', views.workout_calendar, name='workout_calendar'),
]
