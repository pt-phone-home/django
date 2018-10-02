from django.db import models
from datetime import datetime

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

class Website(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    url = models.CharField(max_length=240)

    def __str__(self):
        return self.url

class Genre(models.Model):
    style = models.CharField(max_length=120)

    def __str__(self):
        return self.style