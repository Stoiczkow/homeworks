from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'title', 'content', 'release_date', 'poster', 'director', 'genre', 'actor']