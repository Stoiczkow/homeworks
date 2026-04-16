from django.db import models
from django.utils import timezone


# Zadanie 1 – model Category (normalizacja)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Zadanie 8 – model Tag
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Zadanie 1 – klucz obcy do Category
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='posts',
    )
    # Zadanie 8 – relacja wiele-do-wielu z Tag
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
