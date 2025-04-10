from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class House(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    year = models.IntegerField()