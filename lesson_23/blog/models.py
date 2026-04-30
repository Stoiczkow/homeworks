from django.db import models

# Create your models here.

# task1 
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)#task1
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    class Meta():
        db_table = 'post'

# class Tag_post(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)


#     class Meta():
#         db_table = "tags_posts"
