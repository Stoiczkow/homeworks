from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import View

from .models import Ogloszenia

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world")

def show_product(request, product_id):
    return HttpResponse(f"Twój produkt ma ID {product_id}")

def show_ogloszenia(request):
    ogloszenia = Ogloszenia.objects.all().order_by('-created_at')
    paginator = Paginator(ogloszenia, 1) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'ogloszenia.html', {'page_obj': page_obj})

class hello_world2(View):
    def get(self, request):        
        return HttpResponse("Hello world 2")

def info_view(request):
    return HttpResponse("Informacje o stronie")

def rules_view(request):
    return HttpResponse("Regulamin")

def hello_username_view(request, username):
    return HttpResponse(f"Witaj na profilu, {username}")