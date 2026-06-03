from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_queryset(self):
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')        
        
        if min_price and max_price:
            return Product.objects.filter(price__gte=min_price, price_lte=max_price)
        elif min_price:
            return Product.objects.filter(price__gte=min_price)
        elif min_price:
            return Product.objects.filter(price__lte=max_price)
        else:
            return Product.objects.all()
    
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer    
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

from rest_framework.response import Response
@api_view(['GET'])
def set_name(request):
    response = Response({"message": "Ustawiono ciasteczko!"})
    
    name = request.GET.get("name")
    response.set_cookie('user_name', name, max_age=3600)    
    return response

@api_view(['GET'])
def hello_view(request):
    username = request.COOKIES.get('user_name', 'Gość')
    return Response({"message": f"Witaj, {username}!"})

@api_view(['GET'])
def calculator(request):
    from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def calculator(request):
    try:
        num1 = float(request.query_params.get('num1'))
        num2 = float(request.query_params.get('num2'))
        operation = request.query_params.get('operation')
    except (TypeError, ValueError):
        return Response({
            "result": None,
            "error": "Nieprawidłowe dane wejściowe"
        })

    if operation == 'add':
        result = num1 + num2

    elif operation == 'subtract':
        result = num1 - num2

    elif operation == 'multiply':
        result = num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return Response({
                "result": None,
                "error": "Błąd! Nie można dzielić przez 0"
            })
        result = num1 / num2

    else:
        return Response({
            "result": None,
            "error": "Nieprawidłowa operacja"
        })

    return Response({"result": result})