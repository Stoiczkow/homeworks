from django.db import models

# Create your models here.

class Actor(models.Model):
    name_surname = models.CharField(max_length=200)
    actor_image = models.ImageField(upload_to='movies/actors/')

    def __str__(self):
        return self.name_surname

class Genre(models.Model):
    genre_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.genre_name

class Director(models.Model):
    name_surname = models.CharField(max_length=200)
    actor_image = models.ImageField(upload_to='movies/directors/')

    def __str__(self):
        return self.name_surname


class Movie(models.Model):
    title = models.CharField("Tytul: ", max_length=200, unique=True)
    content = models.TextField("Opis Filmu")
    release_date = models.DateField("Data premiery: ")
    poster = models.ImageField("Plakat: ", upload_to='movies/posters/')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)    
    
    def __str__(self):
        return self.title


