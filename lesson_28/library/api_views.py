from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .models import Book, Reservation
from .serializers import BookSerializer, ReservationSerializer
from .services import ReservationError, release_expired_reservations, reserve_copy_for_user


@extend_schema_view(
    list=extend_schema(
        summary='Lista książek',
        description='Zwraca katalog książek z opcjonalnym filtrowaniem po autorze, gatunku i frazie tekstowej.',
        tags=['Książki'],
        parameters=[
            OpenApiParameter(name='q', description='Fraza wyszukiwania w tytule lub opisie', required=False, type=OpenApiTypes.STR),
            OpenApiParameter(name='author', description='ID autora', required=False, type=OpenApiTypes.INT),
            OpenApiParameter(name='genre', description='ID gatunku', required=False, type=OpenApiTypes.INT),
        ],
    ),
    retrieve=extend_schema(
        summary='Szczegóły książki',
        description='Zwraca pełne informacje o jednej książce.',
        tags=['Książki'],
    ),
)
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """API do przeglądania katalogu biblioteki."""

    serializer_class = BookSerializer
    queryset = Book.objects.select_related('author').prefetch_related('genres', 'copies').all()

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('q', '').strip()
        author_id = self.request.query_params.get('author', '').strip()
        genre_id = self.request.query_params.get('genre', '').strip()

        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)

        return queryset.distinct()


class ReservationListCreateAPIView(APIView):
    """API do przeglądania i tworzenia własnych rezerwacji."""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Moje rezerwacje',
        description='Zwraca listę rezerwacji zalogowanego użytkownika.',
        tags=['Rezerwacje'],
        responses=ReservationSerializer(many=True),
    )
    def get(self, request):
        release_expired_reservations()
        reservations = Reservation.objects.select_related('copy__book').filter(user=request.user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary='Utwórz rezerwację',
        description='Tworzy nową rezerwację dostępnego egzemplarza na 14 dni.',
        tags=['Rezerwacje'],
        request=ReservationSerializer,
        responses={201: ReservationSerializer},
    )
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            reservation = reserve_copy_for_user(serializer.validated_data['copy_id'], request.user)
        except ReservationError as error:
            return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)