from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def show_products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {"products": all_products})

class ShowProducts(View):
    def get(self, request):
        all_products = Product.objects.all()
        return render(request, 'products.html', {"products": all_products})

class AddProduct(View):
    def get(self, request):
        return render(request, 'add_product.html', {"form": ProductForm})
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['desc']
            price = form.cleaned_data['price']

            Product.objects.create(name=name, description=description, price=price)

            return redirect(show_products)
        
class ViewCategory(View):
    def get(self, request, category_int):

        products_from_category = Product.objects.all().filter(category_id = category_int)

        print(products_from_category)

        try:
            category_name = Category.objects.get(id=category_int).name
        except:
            return render(request, 'category.html', {"message": "Nie znaleziono kategorii z tym ID"})

        return render(request, 'category.html', {"name": category_name, "products_from_category": products_from_category})