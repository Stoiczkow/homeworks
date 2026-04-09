from django.shortcuts import render, redirect
from django.views import View

from .models import Product
from .forms import ProductForm

# Create your views here.

def show_products(request):
    all_products = Product.objects.all()
    
    return render(request, 'products.html', {"products": all_products})

class ShowProduct(View):
    def get(self, request):
        all_products = Product.objects.all()
        return render(request, 'products.html', {"products": all_products})
    
class AddProduct(View):
    def get(self, request):
        if request.method == 'GET':
            form = ProductForm()
            
            return render(request, "product_form.html", {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products-view') 
        else:
            return render(request, 'product_form.html', {'form': form, 
                                                    'error': "Nieprawidłowe dane"})
            
def show_products_from_category(request, category_id):
    filtered_products = Product.objects.filter(category=category_id)
    
    return render(request, "products.html", {"products": filtered_products})
    