from django.db import models

from datetime import timedelta
from django.utils import timezone

#task1
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    #task8
    @property
    def is_new(self):
        time_diff = timezone.now() - self.pub_date
        return time_diff < timedelta(days=3)

 

