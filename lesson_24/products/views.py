from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from products.forms import CustomUserCreationForm
from .models import Product

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla {username} zostało utworzone!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@staff_member_required
def admin_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'users/admin_users.html', {'users': users})

@permission_required('products.view_products', raise_exception=True)
@login_required
def all_products(request):
    prods = Product.objects.all()
    return render(request, 'products/all.html', {'products': prods})
