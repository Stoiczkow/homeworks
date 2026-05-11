from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Product2
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            messages.success(request, f"Zarejestrowales sie uzytkowniku {username}")
            login(request, user)
            # return redirect('login')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form" : form} )


@login_required
def home(request):
    return render(request, "home.html")

@staff_member_required 
def users_list(request):


        users = User.objects.all()

        return render(request, "users/users_list.html", {"users" : users})




















# def register(request):

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
            
#             messages.success(request, f"Konto dla {username}" 
#                              f"zostalo utworzone mozesz sie teraz zalogowac") 
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "users/register.html", {"form" : form})



# @permission_required('products.views_product2', raise_exception=True)
# @login_required 
# def all_products(request):

#     products = Product2.objects.all()

#     return render(request, "products/all.html", {"products" : products})

