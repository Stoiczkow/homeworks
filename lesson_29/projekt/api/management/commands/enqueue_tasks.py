import random
from django.core.management.base import BaseCommand
from api.tasks import multiply


# Zadanie 9 – komenda manage.py enqueue_tasks
# Użycie: python manage.py enqueue_tasks
class Command(BaseCommand):
    help = 'Dodaje do kolejki Celery 50 zadań multiply z losowymi argumentami'

    def handle(self, *args, **options):
        for i in range(50):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            task = multiply.delay(a, b)
            self.stdout.write(f"  [{i+1:02d}] multiply({a}, {b}) → task_id={task.id}")

        self.stdout.write(self.style.SUCCESS('Dodano 50 zadań multiply do kolejki Celery.'))
