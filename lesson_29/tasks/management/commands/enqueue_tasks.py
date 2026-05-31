import random
from django.core.management.base import BaseCommand
from faker import Faker
from tasks.tasks import multiply


#task9
class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Rozpoczynam dodawanie zadań...'))

        for i in range(50):
            
            x = random.randint(1, 100)
            y = random.randint(1, 100)

            
            multiply.delay(x, y)

            self.stdout.write(f'Dodano zadanie {i+1}/50: multiply({x}, {y})')

        self.stdout.write(self.style.SUCCESS('Pomyślnie dodano 50 zadań do kolejki!'))