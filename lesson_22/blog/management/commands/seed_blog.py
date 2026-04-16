import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from blog.models import Category, Tag, Post


# Zadanie 7 + 9 – komenda seed_blog z kategoriami, tagami i postami
class Command(BaseCommand):
    help = 'Usuwa stare dane i zasila baze przykladowymi kategoriami, tagami i postami.'

    # Zadanie 7b – predefiniowane kategorie
    CATEGORIES = [
        'Technologia', 'Podroze', 'Kulinaria', 'Sport',
        'Nauka', 'Kultura', 'Zdrowie', 'Motoryzacja',
    ]

    # Zadanie 9 – predefiniowane tagi
    TAGS = [
        'python', 'django', 'web', 'travel', 'food', 'fitness',
        'science', 'music', 'books', 'gaming', 'diy', 'finance',
    ]

    def handle(self, *args, **kwargs):
        fake = Faker('pl_PL')

        # Zadanie 7a – usuniecie wszystkich postow, kategorii i tagow
        self.stdout.write('Usuwanie starych danych...')
        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        # Zadanie 7b – tworzenie predefiniowanych kategorii
        self.stdout.write('Tworzenie kategorii...')
        categories = [
            Category.objects.create(name=name) for name in self.CATEGORIES
        ]
        self.stdout.write(self.style.SUCCESS(f'  Utworzono {len(categories)} kategorii.'))

        # Zadanie 9 – tworzenie tagow
        self.stdout.write('Tworzenie tagow...')
        tags = [Tag.objects.create(name=name) for name in self.TAGS]
        self.stdout.write(self.style.SUCCESS(f'  Utworzono {len(tags)} tagow.'))

        # Zadanie 7c – 100 losowych postow z Faker
        # Zadanie 9 – kazdy post dostaje losowo 1-5 tagow
        self.stdout.write('Tworzenie 100 postow...')
        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6).rstrip('.'),
                content='\n\n'.join(fake.paragraphs(nb=4)),
                category=random.choice(categories),
                published_at=timezone.make_aware(fake.date_time_this_year()),
            )
            # Zadanie 9 – losowo 1-5 tagow
            post.tags.set(random.sample(tags, k=random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS('  Utworzono 100 postow.'))
        self.stdout.write(self.style.SUCCESS('Gotowe!'))
