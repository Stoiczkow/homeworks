from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from .models import Ogloszenie

def hello_world(request):
    return HttpResponse("Hello World")

def show_product(request, product_id):
    return HttpResponse(f"Twój produkt ma ID {product_id}")

class HelloWorld2(View):
    def get(self, request):
        return HttpResponse("To jest odpowiedź z widoku opartego na klasie!")

def show_ogloszenia(request):
    ogloszenia = Ogloszenie.objects.all().order_by('data_dodania')
    paginator = Paginator(ogloszenia, 1) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'ogloszenia.html', {'page_obj': page_obj})