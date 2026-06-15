import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from kino.models import Gatunek, Aktor, Rezyser, Film, Seans, Rezerwacja


class Command(BaseCommand):
    help = 'Populate database with sample data for cinema application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Delete existing sample data before seeding',
        )

    def handle(self, *args, **options):
        if options['reset']:
            self.stdout.write(self.style.WARNING('Resetting existing sample data...'))
            Rezerwacja.objects.all().delete()
            Seans.objects.all().delete()
            Film.objects.all().delete()
            Gatunek.objects.all().delete()
            Aktor.objects.all().delete()
            Rezyser.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Old sample data cleared.'))

        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))

        fake = Faker('pl_PL')
        Faker.seed(1234)
        random.seed(1234)

        # Create genres
        gatunki = {}
        genre_names = ['Akcja', 'Komedia', 'Dramat', 'Horror', 'Sci-Fi', 'Thriller', 'Rodzinny', 'Fantasy']
        for name in genre_names:
            gatunek, created = Gatunek.objects.get_or_create(nazwa=name)
            gatunki[name] = gatunek
            if created:
                self.stdout.write(f'Created genre: {name}')

        # Create actors
        aktorzy = {}
        for _ in range(20):
            actor_name = fake.name()
            aktor, created = Aktor.objects.get_or_create(imie_nazwisko=actor_name)
            aktorzy[actor_name] = aktor
            if created:
                self.stdout.write(f'Created actor: {actor_name}')

        # Create directors
        rezyserzy = {}
        for _ in range(10):
            director_name = fake.name()
            rezyser, created = Rezyser.objects.get_or_create(imie_nazwisko=director_name)
            rezyserzy[director_name] = rezyser
            if created:
                self.stdout.write(f'Created director: {director_name}')

        # Create movies
        filmy = {}
        sample_films = [
            {
                'tytul': 'Podróż w Czasie',
                'opis': 'Fascynująca opowieść o grupie naukowców, którzy odkrywają sposób na podróże w czasie i stają przed wyborem zmiany przeszłości.',
                'data_premiery': fake.date_between(start_date='-5y', end_date='today'),
                'gatunki': ['Sci-Fi', 'Thriller'],
            },
            {
                'tytul': 'Nocne Echo',
                'opis': 'Młoda dziennikarka trafia do małego miasteczka, gdzie zaczynają się dziać przerażające rzeczy.',
                'data_premiery': fake.date_between(start_date='-3y', end_date='today'),
                'gatunki': ['Horror', 'Thriller'],
            },
            {
                'tytul': 'Komedio Karmelowa',
                'opis': 'Łącząca losy sympatycznych bohaterów opowieść o przyjaźni, miłości i słodkich wpadkach.',
                'data_premiery': fake.date_between(start_date='-2y', end_date='today'),
                'gatunki': ['Komedia'],
            },
            {
                'tytul': 'Magiczny Las',
                'opis': 'Rodzinna przygoda w krainie pełnej czarów, gdzie każdy krok może zmienić przyszłość.',
                'data_premiery': fake.date_between(start_date='-1y', end_date='today'),
                'gatunki': ['Fantasy', 'Rodzinny'],
            },
            {
                'tytul': 'Cień Przeszłości',
                'opis': 'Dramat o bohaterze, który musi zmierzyć się z sekretami swojej rodziny.',
                'data_premiery': fake.date_between(start_date='-7y', end_date='today'),
                'gatunki': ['Dramat', 'Thriller'],
            },
            {
                'tytul': 'Kosmiczne Przeznaczenie',
                'opis': 'Epicka historia misji międzygalaktycznej, która zmienia losy całej ludzkości.',
                'data_premiery': fake.date_between(start_date='-4y', end_date='today'),
                'gatunki': ['Sci-Fi', 'Akcja'],
            },
            {
                'tytul': 'Wielka Ucieczka',
                'opis': 'Szybki i dynamiczny thriller, w którym bohaterowie próbują przechytrzyć przeciwników podczas spektakularnej ucieczki.',
                'data_premiery': fake.date_between(start_date='-6y', end_date='today'),
                'gatunki': ['Akcja'],
            },
            {
                'tytul': 'Złodziej Snów',
                'opis': 'Dziwna przygoda w świecie snów, w której prawda miesza się z wyobraźnią.',
                'data_premiery': fake.date_between(start_date='-2y', end_date='today'),
                'gatunki': ['Fantasy', 'Thriller'],
            },
        ]

        for film_data in sample_films:
            rezyser = random.choice(list(rezyserzy.values()))
            film, created = Film.objects.get_or_create(
                tytul=film_data['tytul'],
                defaults={
                    'opis': film_data['opis'],
                    'data_premiery': film_data['data_premiery'],
                    'rezyser': rezyser,
                }
            )
            for gatunek_name in film_data['gatunki']:
                film.gatunek.add(gatunki[gatunek_name])

            wybrani_aktorzy = random.sample(list(aktorzy.values()), k=4)
            for aktor in wybrani_aktorzy:
                film.aktorzy.add(aktor)

            filmy[film.tytul] = film
            if created:
                self.stdout.write(f'Created film: {film.tytul}')

        # Add a few extra films to complete the repertoire
        for _ in range(7):
            tytul = fake.sentence(nb_words=3).rstrip('.')
            opis = fake.paragraph(nb_sentences=3)
            data_premiery = fake.date_between(start_date='-10y', end_date='today')
            rezyser = random.choice(list(rezyserzy.values()))
            film, created = Film.objects.get_or_create(
                tytul=tytul,
                defaults={
                    'opis': opis,
                    'data_premiery': data_premiery,
                    'rezyser': rezyser,
                }
            )

            wybrane_gatunki = random.sample(list(gatunki.values()), k=random.randint(1, 3))
            for gatunek in wybrane_gatunki:
                film.gatunek.add(gatunek)

            wybrani_aktorzy = random.sample(list(aktorzy.values()), k=random.randint(2, 5))
            for aktor in wybrani_aktorzy:
                film.aktorzy.add(aktor)

            filmy[film.tytul] = film
            if created:
                self.stdout.write(f'Created film: {film.tytul}')

        # Create screenings with different dates and times per film
        now = datetime.now()
        possible_hours = [10, 12, 14, 16, 18, 20, 22]
        for film_title, film_obj in filmy.items():
            screening_days = random.sample(range(1, 9), k=4)
            screening_hours = random.sample(possible_hours, k=4)
            for day_offset, hour in zip(screening_days, screening_hours):
                screening_date = now.date() + timedelta(days=day_offset)
                screening_time = datetime.combine(screening_date, datetime.min.time()) + timedelta(hours=hour, minutes=random.choice([0, 15, 30, 45]))
                seans, created = Seans.objects.get_or_create(
                    film=film_obj,
                    czas_rozpoczecia=screening_time,
                    defaults={
                        'cena': round(20.0 + random.uniform(0, 15), 2),
                        'liczba_miejsc': 60,
                        'dostepne_miejsca': 60,
                    }
                )
                if created:
                    self.stdout.write(f'Created screening: {film_title} at {screening_time}')

        # Ensure screenings on 15 June
        special_date = datetime(now.year, 6, 15).date()
        special_hours = [12, 15, 18, 21]
        for film_obj, hour in zip(list(filmy.values())[:4], special_hours):
            screening_time = datetime.combine(special_date, datetime.min.time()) + timedelta(hours=hour)
            seans, created = Seans.objects.get_or_create(
                film=film_obj,
                czas_rozpoczecia=screening_time,
                defaults={
                    'cena': round(20.0 + random.uniform(0, 15), 2),
                    'liczba_miejsc': 60,
                    'dostepne_miejsca': 60,
                }
            )
            if created:
                self.stdout.write(f'Created 15 June screening: {film_obj.tytul} at {screening_time}')

        # Create test users
        user_data = [
            {'username': 'john', 'email': 'john@test.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane', 'email': 'jane@test.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'bob', 'email': 'bob@test.com', 'first_name': 'Bob', 'last_name': 'Johnson'},
        ]

        for data in user_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                }
            )
            if created:
                user.set_password('testpass123')
                user.save()
                self.stdout.write(f"Created user: {data['username']}")

        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully!'))
        self.stdout.write(self.style.WARNING('Test users: john, jane, bob (password: testpass123)'))
        self.stdout.write(self.style.WARNING('Admin user: admin'))
