from django.shortcuts import render
from django.core.cache import cache

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Note, Author, Book
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated

class ProductsViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        min_price = self.request.query_params.get("min_price", )
        max_price = self.request.query_params.get("max_price", )
        
        if min_price and max_price:
            return Product.objects.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
             return Product.objects.filter(price__gte=min_price)
        elif max_price:
             return Product.objects.filter(price__lte=max_price)
        else:
             return Product.objects.all()
             
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    # Cache key dla listy produktów
    PRODUCTS_LIST_CACHE_KEY = 'products_list'
    PRODUCTS_LIST_CACHE_TIMEOUT = 60 * 10  # 10 minut

    # Cache key prefix dla szczegółów produktu
    PRODUCT_DETAIL_CACHE_KEY_PREFIX = 'product_retrieve_'
    PRODUCT_DETAIL_CACHE_TIMEOUT = 60  # 1 minuta

    def list(self, request, *args, **kwargs):
        """Zwróć listę produktów z cache'a lub buforuj odpowiedź"""
        cached_data = cache.get(self.PRODUCTS_LIST_CACHE_KEY)
        
        if cached_data is not None:
            return Response(cached_data)
        
        response = super().list(request, *args, **kwargs)
        cache.set(self.PRODUCTS_LIST_CACHE_KEY, response.data, self.PRODUCTS_LIST_CACHE_TIMEOUT)
        
        return response

    def retrieve(self, request, *args, **kwargs):
        """Zwróć szczegóły produktu z cache'a lub buforuj odpowiedź"""
        product_id = kwargs.get('pk')
        cache_key = f'{self.PRODUCT_DETAIL_CACHE_KEY_PREFIX}{product_id}'
        
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)
        
        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, self.PRODUCT_DETAIL_CACHE_TIMEOUT)
        
        return response

    def perform_update(self, serializer):
        serializer.save()
        self._invalidate_product_caches()

    def perform_partial_update(self, serializer):
        serializer.save()
        self._invalidate_product_caches()

    def _invalidate_product_caches(self):
        product_id = self.kwargs.get('pk')
        
        # Usuń cache dla szczegółów tego konkretnego produktu
        product_cache_key = f'{self.PRODUCT_DETAIL_CACHE_KEY_PREFIX}{product_id}'
        cache.delete(product_cache_key)
        
        # Usuń cache dla listy (bo zawiera ten produkt)
        cache.delete(self.PRODUCTS_LIST_CACHE_KEY)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def setname(request):

    response = Response({"message": "Ustawiono ciasteczko"})    

    name = request.GET.get("name")

    response.set_cookie('username', name, max_age=3600)

    return response

@api_view(["GET"])
def helloview(request):
        
        username = request.COOKIES.get('username', 'Bezi')

        return Response({"message": f"Witaj, {username}!"})

