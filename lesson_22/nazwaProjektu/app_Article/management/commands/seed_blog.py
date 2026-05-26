import random
from django.core.management.base import BaseCommand
from faker import Faker
from app_Article.models import Author, Article, Category, Tag


class Command(BaseCommand):
    help = 'Seeds the database with sample blog data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Czyszczenie starych danych...')
        Article.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()
        self.stdout.write(self.style.WARNING('Stare dane usuniete.'))

        fake = Faker('pl_PL')

        category_names = ['Technologia', 'Podroze', 'Kulinaria', 'Nauka', 'Sport', 'Kultura', 'Biznes']
        categories = []
        for name in category_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)
        self.stdout.write(self.style.SUCCESS(f'{len(categories)} kategorii utworzono.'))

        tag_names = ['django', 'python', 'ai', 'web', 'data', 'linux', 'mobile', 'security', 'travel', 'food']
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        self.stdout.write(self.style.SUCCESS(f'{len(tags)} tagow utworzono.'))

        authors = []
        for _ in range(10):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.unique.email()
            )
            authors.append(author)
        self.stdout.write(self.style.SUCCESS(f'{len(authors)} autorow utworzono.'))

        posts = []
        for _ in range(100):
            post = Article.objects.create(
                title=fake.sentence(nb_words=6),
                content=' '.join(fake.paragraphs(nb=5)),
                author_id=random.choice(authors),
                category_id=random.choice(categories),
                status=random.choice(['published', 'draft']),
            )
            post.tags.set(random.sample(tags, k=random.randint(1, 5)))
            posts.append(post)
        self.stdout.write(self.style.SUCCESS(f'{len(posts)} artykulow utworzono.'))

        self.stdout.write(self.style.SUCCESS('Seeding zakończony.'))
