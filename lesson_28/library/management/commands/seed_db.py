import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from library.models import Author, Book, Copy, Genre, Reservation


class Command(BaseCommand):
    help = 'Generuje przykładowe dane do projektu biblioteki.'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Usuń istniejące dane przed seedowaniem.')
        parser.add_argument('--books', type=int, default=8, help='Liczba książek do wygenerowania.')

    def handle(self, *args, **options):
        faker = Faker('pl_PL')
        book_count = options['books']

        if options['clear']:
            Reservation.objects.all().delete()
            Copy.objects.all().delete()
            Book.objects.all().delete()
            Author.objects.all().delete()
            Genre.objects.all().delete()

        sample_users = []
        for username in ['anna', 'piotr', 'ola']:
            user, created = User.objects.get_or_create(username=username, defaults={'email': f'{username}@example.com'})
            if created:
                user.set_password('Haslo12345!')
                user.save()
            sample_users.append(user)

        genres = []
        for name in ['Fantastyka', 'Kryminał', 'Biografia', 'Historia', 'Sci-Fi', 'Obyczajowa']:
            genre, _ = Genre.objects.get_or_create(name=name)
            genres.append(genre)

        for index in range(book_count):
            author = Author.objects.create(
                full_name=faker.name(),
                biography=faker.paragraph(nb_sentences=4),
            )
            book = Book.objects.create(
                title=faker.sentence(nb_words=4).rstrip('.'),
                description=' '.join(faker.paragraphs(nb=2)),
                publication_date=faker.date_between(start_date='-10y', end_date='today'),
                author=author,
            )
            book.genres.set(random.sample(genres, k=random.randint(1, 2)))

            copies = []
            for copy_number in range(random.randint(1, 3)):
                copy = Copy.objects.create(
                    book=book,
                    inventory_number=f'BOOK-{index + 1:03d}-{copy_number + 1}',
                )
                copies.append(copy)

            if copies and random.choice([True, False]):
                copy = random.choice(copies)
                copy.status = Copy.Status.RESERVED
                copy.save(update_fields=['status'])
                Reservation.objects.create(
                    user=random.choice(sample_users),
                    copy=copy,
                    valid_until=timezone.localdate() + timedelta(days=14),
                )

            if len(copies) > 1 and random.choice([True, False]):
                past_copy = random.choice(copies)
                Reservation.objects.create(
                    user=random.choice(sample_users),
                    copy=past_copy,
                    valid_until=timezone.localdate() - timedelta(days=3),
                    status=Reservation.Status.FINISHED,
                )

        self.stdout.write(self.style.SUCCESS(f'Wygenerowano {book_count} książek oraz dane testowe użytkowników.'))