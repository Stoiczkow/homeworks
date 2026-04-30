import random
from django.core.management.base import BaseCommand
from faker import Faker

# Pamiętaj o imporcie wszystkich modeli
from homeworks.homeworks.lesson_23.blog.models import Post, Category, Tag
#task9
class Command(BaseCommand):
    help = "Seed data - posts, categories and tags"

    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")

        

        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        all_Tags = ["Nowy", "Do usnuniecia", "Stary", "Do poprawy", "Zakazany"]

        created_tags = []
        for tag in all_Tags:
            new_tag = Tag.objects.create(name = tag)
            created_tags.append(new_tag)   

        all_Categories = ["Technologia", "Podroze", "Kulinaria",
                       "Polityka", "Kultura", "Przyroda", "Geografia",
                       "Panstwa", "Oceany", "Biznes"]
        
        create_category = []
        
        for category in all_Categories:
            new_category = Category.objects.create(name=category) 
            create_category.append(new_category)


        created_post = 0

        for _ in range(50):
            new_post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                description=" ".join(fake.paragraphs(nb=5)),
                category=random.choice(create_category),  # Losowy autor z listy
                created_at=fake.date_time_this_year(),
                author=fake.name()
            )
            number_of_tags = random.randint(1, 5)
            selected_tags = random.sample(created_tags, k=number_of_tags)

            new_post.tags.set(selected_tags)

            created_post += 1
        
        print("Dodano")

#task7
# import random
# from django.core.management.base import BaseCommand
# from faker import Faker

# from blog.models import Post, Category

# class Command(BaseCommand):
#     help = "Seed data - posts and categories"

#     def handle(self, *args, **kwargs):
#         fake = Faker("pl_PL")

#         categories = ["Technologia", "Podroze", "Kulinaria",
#                        "Polityka", "Kultura", "Przyroda", "Geografia",
#                        "Panstwa", "Oceany", "Biznes"]

#         Category.objects.all().delete()
#         Post.objects.all().delete()
#         created_categories = []
#         for cate in categories:
#             new_cate = Category.objects.create(name=cate)
#             created_categories.append(new_cate)

#         posts_created = 0
#         for _ in range(100):
#             post = Post.objects.create(
#                 title=fake.sentence(nb_words=6),
#                 description=" ".join(fake.paragraphs(nb=5)),
#                 category=random.choice(created_categories),  # Losowy autor z listy
#                 created_at=fake.date_time_this_year(),
#                 author=fake.name()
#             )
#             posts_created += 1

#         print("Dodano")

# --------------------------------------------------------

#task5
# import random
# from django.core.management.base import BaseCommand
# from faker import Faker

# from blog.models import Post, Category

# class Command(BaseCommand):
#     help = "Seed data - posts and categories"

#     def handle(self, *args, **kwargs):
#         fake = Faker("pl_PL")

#         categories = []

#         for _ in range(10):
#             category = Category.objects.create(
#                 name=fake.company()
#             )
#             categories.append(category)

#         posts_created = 0
#         for _ in range(10):
#             post = Post.objects.create(
#                 title=fake.sentence(nb_words=6),
#                 description=" ".join(fake.paragraphs(nb=5)),
#                 category=random.choice(categories),  # Losowy autor z listy
#                 created_at=fake.date_time_this_year(),
#                 author=fake.name()
#             )
#             posts_created += 1

#         print("Dodano")