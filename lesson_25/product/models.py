from django.db import models

# Zadanie 2 – Prosty model i serializator
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name