from rest_framework import serializers

from .models import Product, Note, Author, Book


class AuthorSerializator(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'




class BookSerializator(serializers.ModelSerializer):
    author = AuthorSerializator(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price']


#task10

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł notatki musi mieć co najmniej 5 znaków.")
        return value