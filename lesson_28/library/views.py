from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm
from .models import Author, Book, Copy, Genre, Reservation
from .services import ReservationError, cancel_reservation, release_expired_reservations, reserve_copy_for_user


def catalog_view(request):
	release_expired_reservations()
	books = Book.objects.select_related('author').prefetch_related('genres', 'copies').all()
	authors = Author.objects.all()
	genres = Genre.objects.all()

	query = request.GET.get('q', '').strip()
	author_id = request.GET.get('author', '').strip()
	genre_id = request.GET.get('genre', '').strip()

	if query:
		books = books.filter(Q(title__icontains=query) | Q(description__icontains=query))
	if author_id:
		books = books.filter(author_id=author_id)
	if genre_id:
		books = books.filter(genres__id=genre_id)

	books = books.distinct()

	return render(
		request,
		'library/catalog.html',
		{
			'books': books,
			'authors': authors,
			'genres': genres,
			'query': query,
			'selected_author': author_id,
			'selected_genre': genre_id,
		},
	)


def book_detail_view(request, pk):
	release_expired_reservations()
	book = get_object_or_404(Book.objects.select_related('author').prefetch_related('genres', 'copies'), pk=pk)
	available_copies = book.copies.filter(status=Copy.Status.AVAILABLE)
	return render(request, 'library/book_detail.html', {'book': book, 'available_copies': available_copies})


def author_detail_view(request, pk):
	author = get_object_or_404(Author.objects.prefetch_related('books__genres'), pk=pk)
	return render(request, 'library/author_detail.html', {'author': author})


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Konto zostało utworzone i jesteś już zalogowany.')
			return redirect('catalog')
	else:
		form = RegisterForm()

	return render(request, 'library/register.html', {'form': form})


@login_required
def reserve_copy_view(request, copy_id):
	if request.method != 'POST':
		return redirect('catalog')

	try:
		reservation = reserve_copy_for_user(copy_id, request.user)
		messages.success(request, f'Zarezerwowałeś egzemplarz {reservation.copy.inventory_number} na 14 dni.')
	except ReservationError as error:
		messages.error(request, str(error))

	return redirect('my-reservations')


@login_required
def cancel_reservation_view(request, pk):
	if request.method != 'POST':
		return redirect('my-reservations')

	reservation = get_object_or_404(Reservation.objects.select_related('copy'), pk=pk, user=request.user)

	try:
		cancel_reservation(reservation, request.user)
		messages.info(request, 'Rezerwacja została anulowana.')
	except ReservationError as error:
		messages.error(request, str(error))

	return redirect('my-reservations')


@login_required
def user_reservations_view(request):
	release_expired_reservations()
	reservations = Reservation.objects.select_related('copy__book').filter(user=request.user)
	current_reservations = reservations.filter(status=Reservation.Status.ACTIVE)
	historical_reservations = reservations.exclude(status=Reservation.Status.ACTIVE)
	return render(
		request,
		'library/reservations.html',
		{
			'current_reservations': current_reservations,
			'historical_reservations': historical_reservations,
		},
	)
