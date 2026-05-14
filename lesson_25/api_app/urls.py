from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AuthorViewSet, BookViewSet, NoteViewSet, ProductViewSet, calculate_view, hello_view, set_name_view

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('notes', NoteViewSet, basename='note')
router.register('authors', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='book')

urlpatterns = router.urls + [
    path('set-name/', set_name_view, name='set-name'),
    path('hello/', hello_view, name='hello'),
    path('calculate/', calculate_view, name='calculate'),
]