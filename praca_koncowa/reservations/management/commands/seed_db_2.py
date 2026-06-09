import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from movies.models import Movie
from reservations.models import Screening 

class Command(BaseCommand):
    help = 'Automatycznie generuje seanse dla filmów'

    def handle(self, *args, **options):
        movies = list(Movie.objects.all())

        if not movies:
            self.stdout.write(self.style.ERROR('Brak filmów w bazie! Uruchom najpierw generator filmów.'))
            return


        hours_pool = ['10:00', '12:00', '14:00', '17:30', '19:00', '20:00', '21:15']
        prices = [12.00, 30.00]

        count = 0
        
        # 1. Generuje seanse na najbliższe 7 dni
        for day_offset in range(7):
            current_date = date.today() + timedelta(days=day_offset)

            # 2. Wybiera 3 filmy na dany dzień
            num_movies_to_pick = min(3, len(movies))
            daily_movies = random.sample(movies, num_movies_to_pick)

            for random_movie in daily_movies:
                # 3. Dla każdego filmu losuje godziny
                chosen_hours = random.sample(hours_pool, 5)
                random_price = random.choice(prices)

                for random_time in chosen_hours:
                    if not Screening.objects.filter(
                        movie=random_movie, 
                        date_screening=current_date, 
                        start_time=random_time
                    ).exists():
                        
                        # Tworzy seans w bazie danych
                        Screening.objects.create(
                            movie=random_movie,
                            date_screening=current_date,
                            start_time=random_time,
                            price=random_price
                        )
                        count += 1

        self.stdout.write(self.style.SUCCESS(f'Sukces! Automatycznie dodano {count} nowych seansów.'))