import random
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Post, Category, Tag, PostTag


class Command(BaseCommand):
    help = "Seed data - posts and categories"
    
    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")
        
        categories = ["Technologia", "Zdrowie", "Podróże", "Kulinaria",
                      "Sport", "Polityka", "Newsy"]
        
        tags = ["poradnik",
                "tutorial",
                "krok-po-kroku",
                "jak-zrobic",
                "wskazowki",
                "najlepsze-praktyki",
                "przydatne",
                "inspiracja",
                "case-study",
                "analiza",
                "podstawy",
                "zaawansowane",
                "dla-poczatkujacych",
                "dla-zaawansowanych",
                "praktyka",
                "narzedzia",
                "trend",
                "aktualnosci",
                "porownanie",
                "top-lista"]
        
        Post.objects.all().delete()
        #DELETE FROM posts
        
        Category.objects.all().delete()
        
        created_categories = []
        for category in categories:
            new_category = Category.objects.create(name=category)
            created_categories.append(new_category)
        
        created_tags = []
        for tag in tags:
            new_tag = Tag.objects.create(name=tag)
            created_tags.append(new_tag)
            
         
        created_posts = []
        for _ in range(100):
            new_post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=" ".join(fake.paragraphs(nb=5)),
                category=random.choice(created_categories),  
                published_date=fake.date_time_this_year(),
                author=fake.name()
            )
            created_posts.append(new_post)
        
        for post in created_posts:
            num_post_tags = random.randint(1,5)
            
            random_tags = random.sample(created_tags, k=min(num_post_tags, len(created_tags)))
            
            for tag in random_tags:
                PostTag.objects.create(post=post, tag=tag)
            
        print("Dodano")