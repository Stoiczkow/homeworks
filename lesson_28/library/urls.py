from django.urls import path

from .views import author_detail_view, book_detail_view, cancel_reservation_view, catalog_view, register_view, reserve_copy_view, user_reservations_view

urlpatterns = [
    path('', catalog_view, name='catalog'),
    path('register/', register_view, name='register'),
    path('books/<int:pk>/', book_detail_view, name='book-detail'),
    path('authors/<int:pk>/', author_detail_view, name='author-detail'),
    path('my-reservations/', user_reservations_view, name='my-reservations'),
    path('copies/<int:copy_id>/reserve/', reserve_copy_view, name='reserve-copy'),
    path('reservations/<int:pk>/cancel/', cancel_reservation_view, name='cancel-reservation'),
]