from django.contrib.auth.models import User
from django.core import validators
from django.db import models


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booksEnabled = models.BooleanField(default=True)
    moviesEnabled = models.BooleanField(default=True)
    videogamesEnabled = models.BooleanField(default=True)


class Item(models.Model):
    TYPE_CHOICES = [
        ('VG', 'Videogame'),
        ('BK', 'Book'),
        ('MV', 'Movie'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0, validators=[
        validators.MaxValueValidator(10)
    ])
