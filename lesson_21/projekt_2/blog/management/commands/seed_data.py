import random
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Post, Category, Tag, PostTag


class Command(BaseCommand):
    help = "Seed data - posts, categories and tags"
    
    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")
        
        # Predefiniowane kategorie
        categories = ["Technologia", "Zdrowie", "Podróże", "Kulinaria",
                      "Sport", "Polityka", "Newsy"]
        
        # Predefiniowane tagi
        tags_data = ["Python", "Django", "Web", "Backend", "Frontend", 
                     "AI", "Machine Learning", "Database", "API", "DevOps",
                     "Tutorial", "News", "Porada", "Opinia", "Analiza"]
        
        # Usuwanie danych
        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()
        PostTag.objects.all().delete()
        
        # Tworzymy kategorie
        created_categories = []
        for category in categories:
            new_category = Category.objects.create(name=category)
            created_categories.append(new_category)
        
        # Tworzymy tagi
        created_tags = []
        for tag in tags_data:
            new_tag = Tag.objects.create(name=tag)
            created_tags.append(new_tag)

        # Tworzymy posty z losowo przypisanymi tagami
        posts_created = 0
        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=" ".join(fake.paragraphs(nb=5)),
                category=random.choice(created_categories),
                published_date=fake.date_time_this_year(),
                author=fake.name()
            )
            posts_created += 1
            
            # Losowo przypisz od 1 do 5 tagów do posta
            num_tags = random.randint(1, 5)
            selected_tags = random.sample(created_tags, min(num_tags, len(created_tags)))
            
            for tag in selected_tags:
                PostTag.objects.create(post=post, tag=tag)
            
        print(f" Dodano {posts_created} postów")
        print(f" Dodano {len(created_categories)} kategorii")
        print(f" Dodano {len(created_tags)} tagów")
        print(f" Przypisano losowe tagi do wszystkich postów (1-5 tagów na post)")