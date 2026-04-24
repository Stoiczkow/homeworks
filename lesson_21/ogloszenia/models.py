from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ogloszenie(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.CharField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul