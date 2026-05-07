from django.http import HttpResponse


def home(request):
    return HttpResponse("Django działa!")


def show_product(request, product_id):
    return HttpResponse(f'Produkt o id: {product_id}')
