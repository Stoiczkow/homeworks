from django.contrib import admin

from .models import Author, Book, Copy, Genre, Reservation


class CopyInline(admin.TabularInline):
	model = Copy
	extra = 1


class ReservationInline(admin.TabularInline):
	model = Reservation
	extra = 0
	readonly_fields = ['reservation_date', 'valid_until']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'book_count']
	search_fields = ['full_name']

	@admin.display(description='Liczba książek')
	def book_count(self, obj):
		return obj.books.count()


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'publication_date', 'available_copies_display', 'genres_display']
	search_fields = ['title', 'author__full_name', 'description']
	list_filter = ['publication_date', 'genres', 'author']
	inlines = [CopyInline]

	@admin.display(description='Dostępne egzemplarze')
	def available_copies_display(self, obj):
		return obj.available_copies_count

	@admin.display(description='Gatunki')
	def genres_display(self, obj):
		return ', '.join(obj.genres.values_list('name', flat=True)) or 'Brak'


@admin.register(Copy)
class CopyAdmin(admin.ModelAdmin):
	list_display = ['inventory_number', 'book', 'status', 'current_reservation_user']
	search_fields = ['inventory_number', 'book__title']
	list_filter = ['status']
	inlines = [ReservationInline]

	@admin.display(description='Aktywna rezerwacja')
	def current_reservation_user(self, obj):
		reservation = obj.reservations.filter(status=Reservation.Status.ACTIVE).select_related('user').first()
		return reservation.user.username if reservation else 'Brak'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ['user', 'copy', 'book_title', 'status', 'reservation_date', 'valid_until']
	search_fields = ['user__username', 'copy__inventory_number', 'copy__book__title']
	list_filter = ['status', 'reservation_date', 'valid_until']

	@admin.display(description='Książka')
	def book_title(self, obj):
		return obj.copy.book.title
