from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Screening(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='screenings', verbose_name="Film")
    date_screening = models.DateField("Data seansu")
    start_time = models.TimeField("Rozpoczecie seansu")
    price = models.DecimalField("Cena za bilet", decimal_places=2, max_digits=4)

    class Meta:
        ordering = ['date_screening', 'start_time']

    def __str__(self):
        return f"{self.movie.title} - {self.date_screening} o {self.start_time}"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('RESERVED', 'Zarezerwowana'),
        ('PAID', 'Opłacona'),
        ('CANCELLED', 'Anulowana'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', verbose_name='uzytkownik')
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE, related_name='reservations', verbose_name='seans')
    number_of_places = models.PositiveIntegerField("Ilość miejsc")
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='RESERVED')
    creat_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Rezerwacja #{self.id} - {self.user.username} ({self.screening.movie.title})"