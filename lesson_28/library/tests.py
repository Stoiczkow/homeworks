from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Author, Book, Copy, Genre, Reservation


class LibraryTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='czytelnik', password='BezpieczneHaslo123')
		self.author = Author.objects.create(full_name='Jan Kowalski', biography='Autor testowy')
		self.genre = Genre.objects.create(name='Fantastyka')
		self.book = Book.objects.create(
			title='Testowa książka',
			description='Opis testowej książki',
			publication_date=timezone.localdate(),
			author=self.author,
		)
		self.book.genres.add(self.genre)
		self.copy = Copy.objects.create(book=self.book, inventory_number='LIB-001')

	def test_book_available_copies_count(self):
		self.assertEqual(self.book.available_copies_count, 1)

	def test_catalog_view_returns_200(self):
		response = self.client.get(reverse('catalog'), {'q': 'Testowa'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Testowa książka')

	def test_logged_user_can_reserve_copy(self):
		self.client.force_login(self.user)
		response = self.client.post(reverse('reserve-copy', args=[self.copy.pk]))
		self.assertRedirects(response, reverse('my-reservations'))
		self.copy.refresh_from_db()
		reservation = Reservation.objects.get(copy=self.copy)
		self.assertEqual(self.copy.status, Copy.Status.RESERVED)
		self.assertEqual(reservation.user, self.user)
		self.assertEqual(reservation.valid_until, timezone.localdate() + timedelta(days=14))

	def test_schema_view_returns_200(self):
		response = self.client.get(reverse('schema'))
		self.assertEqual(response.status_code, 200)
