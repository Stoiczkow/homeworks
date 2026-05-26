from django.db import models


# Zadanie 1 - model Kategoria i Produkt
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.TextField(blank=True)
    kategoria = models.ForeignKey(
        Kategoria,
        on_delete=models.CASCADE,
        related_name='produkty'
    )

    def __str__(self):
        return self.nazwa


# Zadanie 2 - model Notatka z walidacja tytulu
class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul


# Zadanie 5 - modele Autor i Ksiazka z zagniezdzonymi serialajzerami
class Autor(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    rok_wydania = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='ksiazki')

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
