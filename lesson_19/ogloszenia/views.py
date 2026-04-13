from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from .models import Ogloszenia
# Create your views here.


def hello_world(request):
    return HttpResponse("Hello World")

def show_product(request, product_id):
    return HttpResponse(f"Twój produkt ma takie ID {product_id}")

#class HelloWorld2(View):
#    def get(self, request):
#        return HttpResponse("Hello World 2")

def show_ogloszenia(request):
    ogloszenia = Ogloszenia.objects.all().order_by('-created_at') # sorto rosnaco
    # rosnaco z created at a z minus - created_at malejaco czyli najnoowzsze
    paginator = Paginator(ogloszenia, 1) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    # sellect count - spradza ile jest stron
    # slect * from ogloszenia - limit 1 offset 0

    return render(request, 'ogloszenia.html', {'page_obj': page_obj})