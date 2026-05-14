import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = 'Usuwa stare dane i tworzy przykładowe kategorie, tagi oraz posty blogowe.'

    def handle(self, *args, **options):
        fake = Faker('pl_PL')

        self.stdout.write('Czyszczenie danych...')
        Post.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()

        category_names = [
            'Technologia',
            'Podróże',
            'Kulinaria',
            'Sport',
            'Kultura',
            'Nauka',
            'Edukacja',
        ]
        tag_names = [
            'python',
            'django',
            'tutorial',
            'news',
            'tips',
            'backend',
            'frontend',
            'lifestyle',
        ]

        categories = [Category.objects.create(name=name) for name in category_names]
        tags = [Tag.objects.create(name=name) for name in tag_names]

        self.stdout.write('Tworzenie 100 losowych postów...')
        for _ in range(100):
            post = Post.objects.create(
                category=random.choice(categories),
                title=fake.sentence(nb_words=6),
                content='\n\n'.join(fake.paragraphs(nb=4)),
                publication_date=fake.date_time_between(
                    start_date='-180d',
                    end_date='now',
                    tzinfo=timezone.get_current_timezone(),
                ),
                is_published=random.choice([True, True, True, False]),
            )
            post.tags.set(random.sample(tags, k=random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS('Seeder zakończony powodzeniem.'))