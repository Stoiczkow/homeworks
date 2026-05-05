from rest_framework import serializers

from .models import Task, Place


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class PlaceListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"