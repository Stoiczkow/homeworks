from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer

class ProductsViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        min_price = self.request.query_params.get("min_price", )
        max_price = self.request.query_params.get("max_price", )
        
        if min_price and max_price:
            return Product.objects.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
             return Product.objects.filter(price__gte=min_price)
        elif max_price:
             return Product.objects.filter(price__lte=max_price)
        else:
             return Product.objects.all()
             

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def setname(request):

    response = Response({"message": "Ustawiono ciasteczko"})    

    name = request.GET.get("name")

    response.set_cookie('username', name, max_age=3600)

    return response

@api_view(["GET"])
def helloview(request):
        
        username = request.COOKIES.get('username', 'Bezi')

        return Response({"message": f"Witaj, {username}!"})

