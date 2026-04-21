from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.admin.views.decorators import staff_member_required

from .models import Product3
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


#@permission_required('products.view_product3', raise_exception=True)
@staff_member_required
@login_required
def all_products(request):
    products = Product3.objects.all()
    return render(request, 'products/all.html', {'products': products})

@staff_member_required
@login_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'users/all.html', {'users': users})