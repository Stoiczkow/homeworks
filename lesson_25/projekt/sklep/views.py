from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Kategoria, Produkt, Notatka, Autor, Ksiazka
from .serializers import (
    KategoriaSerializer, ProduktSerializer,
    NotatkaSerializer, AutorSerializer, KsiazkaSerializer
)


# Zadanie 1 - ViewSet dla Kategoria i Produkt
class KategoriaViewSet(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer


# Zadanie 1 + Zadanie 6 - ProduktViewSet z filtrowaniem po cenie
class ProduktViewSet(viewsets.ModelViewSet):
    serializer_class = ProduktSerializer

    def get_queryset(self):
        queryset = Produkt.objects.all()
        # Zadanie 6 - filtrowanie po cenie min/max z query params
        cena_min = self.request.query_params.get('cena_min')
        cena_max = self.request.query_params.get('cena_max')
        if cena_min is not None:
            queryset = queryset.filter(cena__gte=cena_min)
        if cena_max is not None:
            queryset = queryset.filter(cena__lte=cena_max)
        return queryset


# Zadanie 2 - ViewSet dla Notatka (z walidacja tytulu w serialajzerze)
class NotatkaViewSet(viewsets.ModelViewSet):
    queryset = Notatka.objects.all()
    serializer_class = NotatkaSerializer


# Zadanie 5 - ViewSety dla Autor i Ksiazka z zagniezdzonymi serialajzerami
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer


# Zadanie 3 - widoki z ciasteczkami (cookies)
@api_view(['GET'])
def ustaw_ciasteczko(request):
    response = Response({'message': 'Ciasteczko zostalo ustawione'})
    response.set_cookie('moje_ciasteczko', 'wartoscCiasteczka', max_age=3600)
    return response


@api_view(['GET'])
def odczytaj_ciasteczko(request):
    wartosc = request.COOKIES.get('moje_ciasteczko', 'Brak ciasteczka')
    return Response({'moje_ciasteczko': wartosc})


@api_view(['GET'])
def usun_ciasteczko(request):
    response = Response({'message': 'Ciasteczko zostalo usuniete'})
    response.delete_cookie('moje_ciasteczko')
    return response


# Zadanie 4 - kalkulator API (@api_view)
@api_view(['POST'])
def kalkulator(request):
    a = request.data.get('a')
    b = request.data.get('b')
    operacja = request.data.get('operacja')

    if a is None or b is None or operacja is None:
        return Response(
            {'error': 'Podaj parametry: a, b, operacja (dodawanie/odejmowanie/mnozenie/dzielenie)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return Response({'error': 'Parametry a i b muszą być liczbami'}, status=status.HTTP_400_BAD_REQUEST)

    if operacja == 'dodawanie':
        wynik = a + b
    elif operacja == 'odejmowanie':
        wynik = a - b
    elif operacja == 'mnozenie':
        wynik = a * b
    elif operacja == 'dzielenie':
        if b == 0:
            return Response({'error': 'Nie mozna dzielic przez zero'}, status=status.HTTP_400_BAD_REQUEST)
        wynik = a / b
    else:
        return Response(
            {'error': 'Nieznana operacja. Dostepne: dodawanie, odejmowanie, mnozenie, dzielenie'},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({'a': a, 'b': b, 'operacja': operacja, 'wynik': wynik})
