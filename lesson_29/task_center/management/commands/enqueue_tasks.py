import random

from django.core.management.base import BaseCommand

from task_center.tasks import multiply


class Command(BaseCommand):
    help = 'Dodaje do kolejki 50 zadań multiply z losowymi argumentami.'

    def handle(self, *args, **options):
        task_ids = []
        for _ in range(50):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            task = multiply.apply_async(args=(a, b))
            task_ids.append(task.id)

        self.stdout.write(self.style.SUCCESS(f'Dodano 50 zadań. Przykładowe ID: {", ".join(task_ids[:5])}'))