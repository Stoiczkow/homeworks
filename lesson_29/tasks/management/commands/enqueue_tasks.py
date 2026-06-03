from django.core.management.base import BaseCommand

from tasks.tasks import multiply
import random

# Zadanie 9 – Masowe tworzenie zadań
# Napisz własną komendę manage.py (np. enqueue_tasks), która w pętli tworzy i dodaje do
# kolejki 50 zadań multiply z losowymi argumentami.
class Command(BaseCommand):
    help = "Dodaje 50 losowych zadań multiply do kolejki Celery"
    
    def handle(self, *args, **options):
        for i in range(50):
            a = random.randint(1,100)
            b = random.randint(1,100)
            
            task_id = multiply.delay(a, b)
            
            self.stdout.write(
                f"Dodano zadanie #{i + 1}: multiply({a}, {b})"
            )
            
        self.stdout.write(
            self.style.SUCCESS(
                "Dodano 50 zadań do kolejki"
            )
        )