from rest_framework import serializers
from .models import Kategoria, Produkt, Notatka, Autor, Ksiazka


# Zadanie 1 - serialajzery dla Kategoria i Produkt
class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id', 'nazwa']


class ProduktSerializer(serializers.ModelSerializer):
    kategoria_nazwa = serializers.StringRelatedField(source='kategoria', read_only=True)

    class Meta:
        model = Produkt
        fields = ['id', 'nazwa', 'cena', 'opis', 'kategoria', 'kategoria_nazwa']


# Zadanie 2 - serialajzer dla Notatka z walidacja tytulu
class NotatkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notatka
        fields = ['id', 'tytul', 'tresc', 'data_utworzenia']

    def validate_tytul(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Tytul musi miec co najmniej 3 znaki.")
        return value


# Zadanie 5 - zagniezdzone serialajzery Autor i Ksiazka
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'imie', 'nazwisko', 'email']


class KsiazkaSerializer(serializers.ModelSerializer):
    autor_info = AutorSerializer(source='autor', read_only=True)

    class Meta:
        model = Ksiazka
        fields = ['id', 'tytul', 'rok_wydania', 'autor', 'autor_info']
