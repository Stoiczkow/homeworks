from django.db import models

# Create your models here.

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
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
