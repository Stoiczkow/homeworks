from django.db import models

class Category(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

def __str__(self):
    return self.title