import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = "Seed blog categories, tags and posts."

    def handle(self, *args, **options):
        fake = Faker("pl_PL")

        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        categories = [
            Category.objects.create(name=name)
            for name in ["Technologia", "Podróże", "Kulinaria", "Sport", "Kultura", "Biznes"]
        ]
        tags = [
            Tag.objects.create(name=name)
            for name in ["django", "python", "poradnik", "inspiracje", "news", "praktyka", "recenzja", "tutorial"]
        ]

        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content="\n\n".join(fake.paragraphs(nb=3)),
                category=random.choice(categories),
            )
            post.tags.set(random.sample(tags, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS("Created 6 categories, 8 tags and 100 posts."))
