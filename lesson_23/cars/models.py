from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealerzy'


class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True, blank=True, related_name='cars')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    owner_website = models.URLField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        db_table = 'cars'
        verbose_name = 'Samochód'
        verbose_name_plural = 'Samochody'
