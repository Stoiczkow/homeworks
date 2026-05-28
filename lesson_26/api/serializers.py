from rest_framework import serializers
from .models import CachedItem
# zadanie 8
class CachedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CachedItem
        fields = ['id', 'name', "description", 'create_at']