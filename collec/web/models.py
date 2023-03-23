from django.contrib.auth.models import User
from django.db import models


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booksEnabled = models.BooleanField(default=True)
    moviesEnabled = models.BooleanField(default=True)
    videogamesEnabled = models.BooleanField(default=True)
