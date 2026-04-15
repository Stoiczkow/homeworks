from gettext import Catalog
from unicodedata import category
from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, 
                                    on_delete=models.CASCADE)
    # category_id = models.ManyToManyField(Category)
    # category_id = models.OneToOneField(Category)

    @property
    def is_new(self):
        return datetime.now() - self.pub_date < 3
    
    def __str__(self):
        return self.title
    
# class ArticleCategory(models.Model):
#     category_id = models.ForeignKey(Category,
#                                     on_delete=models.CASCADE)
#     article_id = models.ForeignKey(Category,
#                                    on_delete=models.CASCADE)



