from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Product, Note, Author, Book
from .serializer import ProductSerializer, NoteSerializer, AuthorSerializator, BookSerializator
# class ProductViewSet(viewsets.ModelViewSet):
#     querysets = Product.objects.all()
#     serializer_class = ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
            
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer




@api_view(['GET'])
def setName(request):

    response = Response({"message" : "Ustawiono ciasteczko"})

    name = request.GET.get('name')

    response.set_cookie('username', name, max_age=3600 )

    return response


@api_view(['GET'])
def helloview(request):

    username = request.COOKIES.get("username", 'Bezimienny')

    return Response({"message" : f"Witaj, {username}!"})



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializator



class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializator




#task 7

@api_view(["GET"])
def calculator(request):

    try:
        num1 = request.query_params.get('num1')
        num2 = request.query_params.get('num2')
        operation = request.query_params.get('operation')
        
        if num1 is None or num2 is None:
            return Response({"error": "Brak parametrów num1 lub num2"}, status=400)
        
        if operation == 'add':
            result = float(num1) + float(num2)
        elif operation == 'subtract':
            result = float(num1) - float(num2)
        elif operation == 'multiply':
            result = float(num1) * float(num2)
        elif operation == 'divide':
            result = float(num1) / float(num2)
        else:
            return Response({"error" : "nieznana  operacja"}, status=400)
        
    
    except ValueError as e:
        return Response({"error" : f"{e}"}, status=400)
    except ZeroDivisionError as e:
        return Response({"error" : f"nie mozna dzielic przez zero"})
    else:
        return Response({"result" : f"{result}"}, status=400)
