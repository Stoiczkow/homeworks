from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Product, Category
from .forms import ProductForm
# Create your views here.
def show_products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", {"products": all_products})
# dodanie widoku zeby były w products 

def show_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category_id=category_id)
    return render(request, "products.html", {"products": products, "category": category})


class ShowProducts(View):
    def get(self, request):
        all_products = Product.objects.all()
        return render(request, "products.html", {"products": all_products})

class AddProduct(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "add_product.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        return render(request, "add_product.html", {"form": form})   