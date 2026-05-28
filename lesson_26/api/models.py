from django.db import models

# Zadanie 8 – Różne czasy cache dla różnych metod ViewSetu
# Stwórz ModelViewSet dla jednego z Twoich modeli. Użyj dekoratora
# @method_decorator(cache_page(...)) tak, aby widok listy (list) był cachowany na 10 minut, a widok szczegółów (retrieve) tylko na 1 minutę. Metody create, update, destroy nie powinny być cachowane w ogóle.
class CachedItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name