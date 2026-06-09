import random
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from faker import Faker
from movies.models import Movie, Director, Genre, Actor

class Command(BaseCommand):
    help = 'Seeds the database with sample data and images'

    def handle(self, *args, **kwargs):
        self.stdout.write('pobieranie zdjęć')
        
        fake = Faker('pl_PL')

        # Pomocnicza funkcja do pobierania prawdziwego zdjęcia z internetu
        def get_fake_image():
            try:
                # Faker generuje URL, pobieramy zawartość tego obrazka
                response = requests.get(fake.image_url(), timeout=5)
                if response.status_code == 200:
                    return ContentFile(response.content)
            except Exception:
                pass
            return None

        # 1. Tworzenie reżyserów
        directors = []
        for i in range(8):
            director = Director.objects.create(
                name_surname=fake.name()
            )
            # Pobieramy i zapisujemy fizyczny plik
            img_file = get_fake_image()
            if img_file:
                director.actor_image.save(f'director_{i}.jpg', img_file, save=True)
            
            directors.append(director)
        
        self.stdout.write(self.style.SUCCESS(f'{len(directors)} directors created.'))

        # 2. Tworzenie gatunków
        genres = []
        for _ in range(6):
            genre = Genre.objects.create(
                genre_name=fake.word()
            )
            genres.append(genre)

        self.stdout.write(self.style.SUCCESS(f'{len(genres)} genres created.'))

        # 3. Tworzenie aktorów
        actors = []
        for i in range(40):
            actor = Actor.objects.create(
                name_surname=fake.name()
            )
            img_file = get_fake_image()
            if img_file:
                actor.actor_image.save(f'actor_{i}.jpg', img_file, save=True)
                
            actors.append(actor)

        self.stdout.write(self.style.SUCCESS(f'{len(actors)} actors created.'))
        
        # 4. Tworzenie filmów i przypisywanie relacji
        movies_count = 20
        for i in range(movies_count):
            random_director = random.choice(directors)

            movie = Movie.objects.create(
                title=fake.sentence(nb_words=3).rstrip('.'),
                content=fake.paragraph(nb_sentences=5),
                release_date=fake.date_between(start_date='today', end_date='+28d'),
                director=random_director
            )
            
            # Pobieramy plakat dla filmu
            img_file = get_fake_image()
            if img_file:
                movie.poster.save(f'poster_{i}.jpg', img_file, save=True)

            # Przypisanie utworzonych Fakerow
            random_genres = random.sample(genres, k=random.randint(1, 3))
            movie.genre.set(random_genres)

            random_actors = random.sample(actors, k=random.randint(3, 8))
            movie.actor.set(random_actors)

        self.stdout.write(self.style.SUCCESS(f'{movies_count} movies created with physical images.'))
