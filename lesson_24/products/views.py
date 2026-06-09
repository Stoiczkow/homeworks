from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Product
from .forms import UserCreationFormWithEmail

def register(request):
    if request.method == 'POST':
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla {username} zostało utworzone! Zostajesz automatycznie zalogowany.')
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationFormWithEmail()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@permission_required('products.view_product', raise_exception=True)
@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all.html', {'products': products})

@staff_member_required
def show_users(request):
    users = User.objects.all().order_by('id')
    return render(request, 'users.html', {'users': users})