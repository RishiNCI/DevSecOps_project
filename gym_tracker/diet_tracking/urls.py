# diet_tracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_list, name='diet_list'),
    path('create/', views.diet_create, name='diet_create'),
    path('<int:pk>/', views.diet_detail, name='diet_detail'),
    path('<int:pk>/edit/', views.diet_edit, name='diet_edit'),
    path('<int:pk>/delete/', views.diet_delete, name='diet_delete'),
    path('summary/', views.diet_summary, name='diet_summary'),
]
