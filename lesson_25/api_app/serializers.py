from rest_framework import serializers

from .models import Author, Book, Note, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at']
        read_only_fields = ['created_at']

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError('Tytuł notatki musi mieć co najmniej 5 znaków.')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=Author.objects.all(), write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'author_id']