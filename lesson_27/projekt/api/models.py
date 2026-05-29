from django.db import models


class Artykul(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data_dodania = models.DateTimeField(auto_now_add=True)
    data_aktualizacji = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tytul
