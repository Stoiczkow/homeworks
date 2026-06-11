from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.serializers import ProductSerializer
from product.models import Product

# Zadanie 3 ViewSet i Router
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Zadanie 5 - Widok z ciasteczkiem
@api_view(['GET'])
def hello_view(request):
    name = request.COOKIES.get('user_name', "Gość")

    return Response({"message": f"Witaj, {name}"})


@api_view(['GET'])
def set_name_view(request):
    name = request.GET.get('name')
    response = Response({'message': "Ciasteczko utworzone"})

    if name:
        response.set_cookie('user_name', name, max_age=2400)
    return response