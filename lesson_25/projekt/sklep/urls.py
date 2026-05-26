from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    KategoriaViewSet, ProduktViewSet, NotatkaViewSet,
    AutorViewSet, KsiazkaViewSet,
    ustaw_ciasteczko, odczytaj_ciasteczko, usun_ciasteczko,
    kalkulator,
)

router = DefaultRouter()
router.register('kategorie', KategoriaViewSet, basename='kategoria')
router.register('produkty', ProduktViewSet, basename='produkt')
router.register('notatki', NotatkaViewSet, basename='notatka')
router.register('autorzy', AutorViewSet, basename='autor')
router.register('ksiazki', KsiazkaViewSet, basename='ksiazka')

urlpatterns = router.urls + [
    # Zadanie 3 - ciasteczka
    path('ciasteczko/ustaw/', ustaw_ciasteczko, name='ustaw-ciasteczko'),
    path('ciasteczko/odczytaj/', odczytaj_ciasteczko, name='odczytaj-ciasteczko'),
    path('ciasteczko/usun/', usun_ciasteczko, name='usun-ciasteczko'),
    # Zadanie 4 - kalkulator
    path('kalkulator/', kalkulator, name='kalkulator'),
]
