from django.db import models

class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # jeden do wielu
    category = models.ForeignKey(Category, 
                                    on_delete=models.CASCADE)
   
   # inna mteoda 1 do 1 dodajemy powyzej
   #  unique=True)

   # lub 1 do 1 inna metoda
    # cattegory_id = models.OneToOneField(Category)
   
    # wiele do wielu - to many nie widzimy w kodzie będzie w bazie  ,dodaje dziwną nazwę 

    # category_id = models.ManyToManyField(Category)

# tworzenie realcji jedn do wielu
# usuniecie kategorii z bazy usunie automatycznie wsyzstkie artykuły 

    def __str__(self):
        return self.title


# relacja wiele do wielu    - ta metoda lepsza ręczna jawna możemy dodwać dodatkowe pola 
# class ArticleCategory(models.Model):
#     category_id =  models.ForeignKey(Category, 
#                                     on_delete=models.CASCADE)
#     article_id = models.ForeignKey(Category, 
#                                     on_delete=models.CASCADE)

