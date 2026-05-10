from django.test import TestCase


# Create your tests here.
from django.db import models
from django.core.cache import cache

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def post_save(self, record, instance):
        cache.clear()
        # cache.delete(f"task_{instance.id}")

        # print(f"Task '{self.title}' has been saved.")
        return instance
    
    def save(self, *args, **kwargs):
        cache.clear()
        return super().save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Autor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class PlaceArchive(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
