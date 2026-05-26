from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cars'
    )

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
