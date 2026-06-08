from django.core.management.base import BaseCommand
from faker import Faker
import random
from blog.models import Post, Category, PostTag, Tag

class Command(BaseCommand):
    help = "Seed data - posts and categories"

    def handle(self, *args, **kwargs):

        ### Generate data

        fake = Faker("pl_PL")

        categories = []

        for _ in range(10):
            category = Category.objects.create(name = fake.word())
            categories.append(category)


        posts_created = 0
        for _ in range(50):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=" ".join(fake.paragraphs(nb=5)),
                category=random.choice(categories),
                published_date=fake.date_time_this_year(),
                author=fake.name()
            )
            posts_created += 1
            
        print("Dodano")

        ### Generate tags
        tags = list(Tag.objects.all())
        posts = list(Post.objects.all())

        for post in posts:
            seed = random.randint(1,5)
            try:
                drawed_tags = random.sample(tags, seed)
            except ValueError:
                print("Not enough tags available")
                return
            for tag in drawed_tags:
                PostTag.objects.get_or_create(post=post, tag=tag)