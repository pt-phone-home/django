from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.last_name

class Sign_up(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Drinks(models.Model):
    beer = models.CharField(max_length=50)
    wine = models.CharField(max_length=50)

    def __str__(self):
        return self.beer





