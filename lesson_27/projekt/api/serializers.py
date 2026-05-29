from rest_framework import serializers
from .models import Artykul


class ArtkulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artykul
        fields = ['id', 'tytul', 'tresc', 'data_dodania', 'data_aktualizacji']
