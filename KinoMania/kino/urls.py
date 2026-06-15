from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filmy/', views.FilmyListView.as_view(), name='filmy_lista'),
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('seanse/', views.SeansyListView.as_view(), name='seanse_lista'),
    path('seans/<int:pk>/', views.RezerwacjaDetailView.as_view(), name='seans_detail'),
    path('rezerwuj/<int:seans_id>/', views.rezerwuj_bilet, name='rezerwuj_bilet'),
    path('rezerwacje/', views.moje_rezerwacje, name='rezerwacje_lista'),
    path('rezerwacja/<int:rezerwacja_id>/anuluj/', views.anuluj_rezerwacje, name='anuluj_rezerwacje'),
    path('rezerwacja/<int:rezerwacja_id>/potwierdz/', views.potwierdz_rezerwacje, name='potwierdz_rezerwacje'),
    path('register/', views.register, name='register'),
]
