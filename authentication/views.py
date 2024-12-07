# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'authentication/profile.html', {'form': form})

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    bmi = user_profile.calculate_bmi()
    diet_suggestion = user_profile.get_diet_suggestion()  # Get diet suggestion
    context = {'user_profile': user_profile, 'bmi': bmi, 'diet_suggestion': diet_suggestion}
    return render(request, 'authentication/profile.html', context)
