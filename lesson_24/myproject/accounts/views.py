from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegisterForm


# zadanie 5 - strona glowna tylko dla zalogowanych
@login_required
def home(request):
    return render(request, 'home.html')


# zadanie 3 - strona profilu chroniona @login_required
@login_required
def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        # zadanie 6 - uzycie wlasnego formularza z email
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # zadanie 9 - automatyczne logowanie po rejestracji
            login(request, user)
            messages.success(request, f'Konto zostalo utworzone. Witaj, {user.username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


# zadanie 10 - lista uzytkownikow tylko dla staff
@staff_member_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
