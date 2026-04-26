from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
permission_required

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login

from .models import Product
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla {username} zostało utworzone! Jesteś teraz zalogowany.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')


#@permission_required("products.view_product", raise_exception=True) # sprawdza od góry do dołu czy jesteśmy najpierw zalogowani i sprawdza perrmisions
@staff_member_required
@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all.html', {'products': products})