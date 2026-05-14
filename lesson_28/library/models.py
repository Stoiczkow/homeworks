from django.conf import settings
from django.db import models


class Author(models.Model):
	full_name = models.CharField(max_length=200)
	biography = models.TextField(blank=True)
	photo = models.ImageField(upload_to='authors/', blank=True, null=True)

	class Meta:
		ordering = ['full_name']

	def __str__(self):
		return self.full_name


class Genre(models.Model):
	name = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	publication_date = models.DateField()
	cover = models.ImageField(upload_to='covers/', blank=True, null=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
	genres = models.ManyToManyField(Genre, related_name='books', blank=True)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

	@property
	def available_copies_count(self):
		return self.copies.filter(status=Copy.Status.AVAILABLE).count()


class Copy(models.Model):
	class Status(models.TextChoices):
		AVAILABLE = 'available', 'Dostępny'
		RESERVED = 'reserved', 'Zarezerwowany'
		BORROWED = 'borrowed', 'Wypożyczony'

	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
	inventory_number = models.CharField(max_length=50, unique=True)
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)

	class Meta:
		ordering = ['inventory_number']

	def __str__(self):
		return f'{self.book.title} ({self.inventory_number})'


class Reservation(models.Model):
	class Status(models.TextChoices):
		ACTIVE = 'active', 'Aktywna'
		CANCELLED = 'cancelled', 'Anulowana'
		FINISHED = 'finished', 'Zakończona'

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
	copy = models.ForeignKey(Copy, on_delete=models.CASCADE, related_name='reservations')
	reservation_date = models.DateField(auto_now_add=True)
	valid_until = models.DateField()
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

	class Meta:
		ordering = ['-reservation_date']

	def __str__(self):
		return f'{self.user} - {self.copy}'
