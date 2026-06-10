from rest_framework import serializers

from .models import Product, Note, Author, Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['title', 'content', 'created_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title is too short! It should be at least 5 chars")
        return value
        

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'      
        
        
class AuthorBookSerializer(AuthorSerializer):
    pass
        
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorBookSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'

class CalcSerializer(serializers.Serializer):
    num1 = serializers.DecimalField(max_digits=10, decimal_places=4)
    num2 = serializers.DecimalField(max_digits=10, decimal_places=4)
    operation = serializers.ChoiceField(choices=["add", "subtract", "multiply", "divide"])

    def validate(self, data):
        if data['operation'] == "divide" and data['num2'] == 0:
            raise serializers.ValidationError("You can't divide by zero")
        return data