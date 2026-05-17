from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset =  Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
@api_view(['GET'])
def set_name(request):
    name = request.query_params.get('name')

    if not name:
        return Response({"error": "Podaj parametr name, np. /api/set-name/?name=Daniel"}, status=400)

    response = Response({"message": f"Zapisano imię: {name}"})
    response.set_cookie('user_name', name, max_age=3600)
    return response


@api_view(['GET'])
def hello(request):
    name = request.COOKIES.get('user_name', 'Gość')
    return Response({"message": f"Witaj, {name}!"})

@api_view(['GET'])
def calculate(request):
    num1 = request.query_params.get('num1')
    num2 = request.query_params.get('num2')
    operation = request.query_params.get('operation')

    if not num1 or not num2 or not operation:
        return Response(
            {"error": "Podaj num1, num2, operation."},
            status=400
        )
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return Response(
        {"error": "num1 i num2 muszą być liczbami."}
    )

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return Response(
                {"error": "Nie można dzielić przez zero"}
            )
        result = num1 / num2
    else:
        return Response(
            {"error": "Niepoprawna operacja. Użyj: add, subtract, multiply albo divide."}, status=400
        )


    return Response({"result": result})