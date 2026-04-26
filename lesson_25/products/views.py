from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def setname(request):
    response = Response({"message": "Ustawiono ciasteczko"})
    name = request.GET.get('name')
    response .set_cookie('username', name, max_age=3600)
    return response

@api_view(['GET'])
def helloview(request):
    username = request.COOKIES.get('username', 'Gość')
    return Response({"message": f"Witaj {username}"})

def calculate(request):
    try:
        num1 = float(request.GET.get('num1'))
        num2 = float(request.GET.get('num2'))
        operation = request.GET.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return Response({"error": "Nie można dzielić przez zero"})
            result = num1 / num2
        else:
            return Response({"error": "Niepoprawna operacja"})

        return Response({"result": result})
    
    except TypeError:
        return Response({"error": "Brak wymaganych parametrów"})
    


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer