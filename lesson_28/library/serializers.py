from rest_framework import serializers

from .models import Book, Reservation


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name', read_only=True)
    genres = serializers.StringRelatedField(many=True, read_only=True)
    available_copies = serializers.IntegerField(source='available_copies_count', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'publication_date', 'author', 'genres', 'available_copies']


class ReservationSerializer(serializers.ModelSerializer):
    copy_id = serializers.IntegerField(write_only=True)
    copy_inventory_number = serializers.CharField(source='copy.inventory_number', read_only=True)
    book_title = serializers.CharField(source='copy.book.title', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'copy_id',
            'copy_inventory_number',
            'book_title',
            'reservation_date',
            'valid_until',
            'status',
        ]
        read_only_fields = ['reservation_date', 'valid_until', 'status']