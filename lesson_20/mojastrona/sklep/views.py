from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm


def info_view(request):
    return HttpResponse("Informacje o stronie")


def rules_view(request):
    return HttpResponse("Regulamin")


def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })
