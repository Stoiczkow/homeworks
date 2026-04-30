from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.

#task1 - reszta zadania w pliku urls.py
def info_(request):
    return HttpResponse(f"Informacje o stronie")

def rules_(request):
    return HttpResponse(f"Regulamin")
#task2
def user_(request, user_name):
    return HttpResponse(f"Witaj na profilu {user_name}")

#task4 - reszta w urls i templates
def show_product(request):
    all_products = Product.objects.all()
    return render(request, "product.html", {"products":all_products})

#task7


def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price']
            )
            return redirect("product_list")
    else:    
        form = ProductForm()
    return render(request, "product/add_product.html", {"form" : form})

def product_list(request):
    form = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': form})

#task9

def category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, "product/product_list.html", {"products" : products})



