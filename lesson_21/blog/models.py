from django.db import models
from django.utils import timezone


# Zadanie 1 – model Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Zadanie 7 – relacja Article -> Category
# Zadanie 8 – pole is_published i published_at
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # Zadanie 8
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_new(self):
        """Zwraca True jeśli artykuł opublikowany w ciągu ostatnich 3 dni."""
        return self.published_at >= timezone.now() - timezone.timedelta(days=3)