from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from apps.products.models import Product, Note, Author, Book
from apps.products.serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
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
    name = request.GET.get('name')
    response = Response({
        "message": "ustawiono name",
    })
    if name:
        response.set_cookie('user_name', name, max_age=3600)
    return response


@api_view(['GET'])
def hello_view(request):
    user_name = request.COOKIES.get('user_name', 'Gość')
    return Response({
        "message": f"Witaj, {user_name}!"
    })

@api_view(['GET'])
def calculate(request):
    num1 = request.query_params.get('num1')
    num2 = request.query_params.get('num2')
    operation = request.query_params.get('operation')

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except (TypeError, ValueError):
        return Response({
            "error": "Params num1 and num2 must be numbers."
        }, status=status.HTTP_400_BAD_REQUEST)

    result = None

    if operation == 'add':
        result = num1_float + num2_float
    elif operation == 'subtract':
        result = num1_float - num2_float
    elif operation == 'multiply':
        result = num1_float * num2_float
    elif operation == 'divide':
        try:
            result = num1_float / num2_float
        except ZeroDivisionError as e:
            return Response({
                "error": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            "error": f"Operation: {operation} not supported"
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "result": result
    })

#  http://127.0.0.1:8000/api/calculate/?num1=10&num2=5&operation=add
#  http://127.0.0.1:8000/api/calculate/?num1=10&num2=5&operation=subtract
#  http://127.0.0.1:8000/api/calculate/?num1=4&num2=2&operation=multiply
#  http://127.0.0.1:8000/api/calculate/?num1=10&num2=2&operation=divide
#  error wrong num1 or num2  http://127.0.0.1:8000/api/calculate/?num1=4&num2=a&operation=multiply
#  error div by 0  http://127.0.0.1:8000/api/calculate/?num1=10&num2=0&operation=divide
#  error wrong operator  http://127.0.0.1:8000/api/calculate/?num1=10&num2=5&operation=power
