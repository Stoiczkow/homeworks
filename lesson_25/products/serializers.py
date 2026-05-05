from rest_framework import serializers

from .models import Product, Note, Author, Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Tytuł notatki najmniej 5 znaków.')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorBookSerializer(AuthorSerializer):
    class Meta:
        model = Author
        fields = ["name"]
        
        
class BookSerializer(serializers.ModelSerializer):
    #pass
    author = AuthorBookSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'