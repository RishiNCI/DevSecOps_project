# gym_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('workouts/', include('workout_tracking.urls')),
    path('diet/', include('diet_tracking.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
