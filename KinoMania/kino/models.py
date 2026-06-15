from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Gatunek(models.Model):
    """Genre/Category of movies"""
    nazwa = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

    def __str__(self):
        return self.nazwa


class Aktor(models.Model):
    """Actor model"""
    imie_nazwisko = models.CharField(max_length=200)
    zdjecie = models.ImageField(
        upload_to='aktorzy/', 
        blank=True, 
        null=True,
        help_text="Zdjęcie aktora"
    )

    class Meta:
        verbose_name = "Aktor"
        verbose_name_plural = "Aktorzy"

    def __str__(self):
        return self.imie_nazwisko


class Rezyser(models.Model):
    """Director model"""
    imie_nazwisko = models.CharField(max_length=200)
    zdjecie = models.ImageField(
        upload_to='rezyserzy/', 
        blank=True, 
        null=True,
        help_text="Zdjęcie reżysera"
    )

    class Meta:
        verbose_name = "Reżyser"
        verbose_name_plural = "Reżyserzy"

    def __str__(self):
        return self.imie_nazwisko


class Film(models.Model):
    """Movie model"""
    tytul = models.CharField(max_length=200)
    opis = models.TextField()
    data_premiery = models.DateField()
    plakat = models.ImageField(
        upload_to='plakaty/', 
        blank=True, 
        null=True,
        help_text="Plakat filmu"
    )
    gatunek = models.ManyToManyField(Gatunek, related_name='filmy')
    aktorzy = models.ManyToManyField(Aktor, related_name='filmy')
    rezyser = models.ForeignKey(Rezyser, on_delete=models.SET_NULL, null=True, related_name='filmy')
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"
        ordering = ['-data_premiery']

    def __str__(self):
        return self.tytul


class Seans(models.Model):
    """Screening/Session model"""
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='seanse')
    czas_rozpoczecia = models.DateTimeField()
    cena = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Cena biletu w złotówkach"
    )
    liczba_miejsc = models.IntegerField(default=50, validators=[MinValueValidator(1)])
    dostepne_miejsca = models.IntegerField(default=50)

    class Meta:
        verbose_name = "Seans"
        verbose_name_plural = "Seanse"
        ordering = ['czas_rozpoczecia']

    def __str__(self):
        return f"{self.film.tytul} - {self.czas_rozpoczecia}"

    def zmien_dostepne_miejsca(self, ilosc):
        """Update available seats"""
        self.dostepne_miejsca -= ilosc
        self.save()


class Rezerwacja(models.Model):
    """Reservation model"""
    STATUS_CHOICES = [
        ('pending', 'Oczekująca'),
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
        ('completed', 'Zaakceptowana'),
    ]

    seans = models.ForeignKey(Seans, on_delete=models.CASCADE, related_name='rezerwacje')
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rezerwacje')
    ilosc_miejsc = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    data_rezerwacji = models.DateTimeField(auto_now_add=True)
    data_modificacji = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"
        ordering = ['-data_rezerwacji']

    def __str__(self):
        return f"{self.uzytkownik.username} - {self.seans.film.tytul} ({self.ilosc_miejsc} miejsc)"

    def confirm(self):
        """Confirm reservation"""
        if self.status == 'pending':
            self.status = 'confirmed'
            self.save()

    def cancel(self):
        """Cancel reservation and free up seats"""
        if self.status != 'cancelled':
            self.seans.dostepne_miejsca += self.ilosc_miejsc
            self.seans.save()
            self.status = 'cancelled'
            self.save()

