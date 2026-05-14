from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


@login_required
def home_view(request):
	return render(request, 'users/home.html')


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, f'Konto dla {user.username} zostało utworzone.')
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()

	return render(request, 'users/register.html', {'form': form})


def logout_view(request):
	logout(request)
	messages.info(request, 'Zostałeś wylogowany.')
	return redirect('login')


@login_required
def profile_view(request):
	return render(request, 'users/profile.html')


@staff_member_required
def staff_user_list_view(request):
	users = User.objects.all().order_by('username')
	return render(request, 'users/user_list.html', {'users': users})
