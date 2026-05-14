from decimal import Decimal, InvalidOperation

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Author, Book, Note, Product
from .serializers import AuthorSerializer, BookSerializer, NoteSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer

	def get_queryset(self):
		queryset = Product.objects.all().order_by('id')
		min_price = self.request.query_params.get('min_price')
		max_price = self.request.query_params.get('max_price')

		if min_price:
			queryset = queryset.filter(price__gte=self._parse_decimal(min_price, 'min_price'))
		if max_price:
			queryset = queryset.filter(price__lte=self._parse_decimal(max_price, 'max_price'))

		return queryset

	def _parse_decimal(self, value, field_name):
		try:
			return Decimal(value)
		except InvalidOperation as error:
			raise ValidationError({field_name: 'Podaj poprawną liczbę dziesiętną.'}) from error


class NoteViewSet(viewsets.ModelViewSet):
	queryset = Note.objects.all().order_by('-created_at')
	serializer_class = NoteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all().order_by('name')
	serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.select_related('author').all().order_by('title')
	serializer_class = BookSerializer


@api_view(['GET'])
def set_name_view(request):
	name = request.query_params.get('name')
	if not name:
		return Response({'error': 'Parametr name jest wymagany.'}, status=status.HTTP_400_BAD_REQUEST)

	response = Response({'message': f'Ustawiono imię: {name}'})
	response.set_cookie('user_name', name, max_age=3600)
	return response


@api_view(['GET'])
def hello_view(request):
	user_name = request.COOKIES.get('user_name', 'Gość')
	return Response({'message': f'Witaj, {user_name}!'})


@api_view(['GET'])
def calculate_view(request):
	num1 = request.query_params.get('num1')
	num2 = request.query_params.get('num2')
	operation = request.query_params.get('operation')

	if num1 is None or num2 is None or operation is None:
		return Response(
			{'error': 'Podaj num1, num2 oraz operation.'},
			status=status.HTTP_400_BAD_REQUEST,
		)

	try:
		first_number = Decimal(num1)
		second_number = Decimal(num2)
	except InvalidOperation:
		return Response({'error': 'num1 i num2 muszą być liczbami.'}, status=status.HTTP_400_BAD_REQUEST)

	if operation == 'add':
		result = first_number + second_number
	elif operation == 'subtract':
		result = first_number - second_number
	elif operation == 'multiply':
		result = first_number * second_number
	elif operation == 'divide':
		if second_number == 0:
			return Response({'error': 'Nie można dzielić przez zero.'}, status=status.HTTP_400_BAD_REQUEST)
		result = first_number / second_number
	else:
		return Response(
			{'error': 'Dozwolone operacje: add, subtract, multiply, divide.'},
			status=status.HTTP_400_BAD_REQUEST,
		)

	if result == result.to_integral():
		normalized_result = int(result)
	else:
		normalized_result = float(result)

	return Response({'result': normalized_result})
