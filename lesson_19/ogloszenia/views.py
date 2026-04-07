from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World")

def show_products(request, product_id):
    return HttpResponse(f"Twój produkt ma takie ID {product_id}")
