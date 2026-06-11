from django.shortcuts import render
from rest_framework import viewsets

from lesson_25.product.serializers import ProductSerializer
from product.models import Product

# Zadanie 3 ViewSet i Router
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
