from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')

            messages.success(request, f'Konto dla {username} zostało utworzone! Możesz się teraz zalogować.')
            return redirect('login') 

        else:
            form = UserCreationForm()
            return render(request, 'users/register.html', {'form': form})

# Zadanie 5
@login_required
def home(request):
    return render(request, 'home.html')

# Zadanie 3
@login_required
def profile(request):
    return render(request, 'users/profile.html') 