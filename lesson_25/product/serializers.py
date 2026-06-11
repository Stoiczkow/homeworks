from rest_framework import serializers

from product.models import Product

# Zadanie 2 – Prosty model i serializator
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']