import random

from django.core.management.base import BaseCommand

from tasks.tasks import multiply


class Command(BaseCommand):
    help = "Enqueue 50 random multiply tasks."

    def handle(self, *args, **options):
        for _ in range(50):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            multiply.delay(a, b)

        self.stdout.write(self.style.SUCCESS("Enqueued 50 multiply tasks."))
