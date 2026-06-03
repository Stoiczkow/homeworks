from rest_framework import serializers

from .models import Product, Note, Author, Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        value = value.strip()
        
        if len(value) < 5:
            raise serializers.ValidationError("Tytuł musi mieć co najmniej 5 znaków.")
        
        return value
        
    class Meta:
        model = Note
        fields = '__all__'
        

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'      
        
        
class AuthorBookSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Book
        fields = '__all__'        
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorBookSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'