from django.db import models

# Create your models here.

class Ogloszenie(models.Model):
    title = models.CharField(max_length=200)
    opis = models.TextField(max_length=10000)
    cena = models.DecimalField(decimal_places=2, max_digits=8)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'ogloszenia'