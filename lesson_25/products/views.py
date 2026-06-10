from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer, CalcSerializer

from rest_framework.permissions import IsAuthenticated


# W ViewSet dla produktów (z zadania 2) zaimplementuj filtrowanie po cenie. Chcemy móc
# wysyłać zapytania takie jak /api/products/?min_price=100&max_price=200, które zwrócą
# produkty w danym przedziale cenowym. Wskazówka: nadpisz metodę get_queryset w
# swoim ViewSet

class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
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
    queryset = Note.objects.all()
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


@api_view(['GET'])
def helloview(request):
    
    username = request.COOKIES.get('username', 'Bezimienny')

    return Response({"message": f"Witaj, {username}!"})

@api_view(['GET'])
def calc_view(request):
    serializer = CalcSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    validated_data = serializer.validated_data
    num1 = validated_data['num1']
    num2 = validated_data['num2']
    operation = validated_data['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2

    return Response({"result": f"{float(result)}"})