"""
Zadanie 9: komenda do masowego enqueue 50 zadan multiply z losowymi argumentami.

Uzycie:
    python manage.py enqueue_tasks
    python manage.py enqueue_tasks --count 200
"""
import random

from django.core.management.base import BaseCommand

from apps.tasks_app.tasks import multiply


class Command(BaseCommand):
    help = 'Wyslij N (domyslnie 50) zadan multiply z losowymi argumentami do kolejki Celery.'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='ile zadan dodac (domyslnie 50)')

    def handle(self, *args, **options):
        count = options['count']
        task_ids = []
        for _ in range(count):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            async_result = multiply.delay(a, b)
            task_ids.append(async_result.id)
        self.stdout.write(self.style.SUCCESS(f'Dodano {count} zadan multiply do kolejki.'))
        self.stdout.write(f'Pierwsze 3 task_id: {task_ids[:3]}')