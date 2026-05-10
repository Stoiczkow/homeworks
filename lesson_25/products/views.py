from asyncio import Task

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from lesson_25.products.serializers import ProductSerializer


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    