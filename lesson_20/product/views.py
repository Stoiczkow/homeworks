from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from product.forms import ProductForm

from product.models import Product


class InfoView(View):
    def get(self, request):
        return HttpResponse('info view')


class RulesView(View):
    def get(self, request):
        return HttpResponse('rules view')


class UserView(View):
    def get(self, request, username):
        return HttpResponse(f"username: {username}")


class ProductView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'


class ProductCreateFormView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products-view')


class CategoryProductFilter(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id)