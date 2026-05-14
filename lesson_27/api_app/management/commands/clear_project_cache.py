from django.core.cache import cache, caches
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Czyści cache locmem i filebased używane w lesson_27.'

    def handle(self, *args, **options):
        cache.clear()
        caches['filebased'].clear()
        self.stdout.write(self.style.SUCCESS('Cache projektu został wyczyszczony.'))