from rest_framework import serializers
from .models import Task, Place

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']

class PlaceListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
