from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booksEnabled = models.BooleanField(default=True)
    moviesEnabled = models.BooleanField(default=True)
    videogamesEnabled = models.BooleanField(default=True)
    class Meta:

        verbose_name_plural = "settings"


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


class BookDetails(models.Model):
    OWNED_CHOICES = [
        ('', ''),
        ('PH', 'Physical'),
        ('EB', 'E-book'),
        ('NO', 'Not owned'),
    ]

    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=250)
    owned = models.CharField(max_length=2, default='', choices=OWNED_CHOICES)

    class Meta:
        verbose_name_plural = "book details"

    def clean(self):
        if self.item.type != 'BK':
            raise ValidationError('Book details added to a non-book item')


class VideogameDetails(models.Model):
    OWNED_CHOICES = [
        ('', ''),
        ('PH', 'Physical'),
        ('DG', 'Digital'),
        ('SB', 'Subscription'),
        ('NO', 'Not owned'),
    ]

    PLATFORM_CHOICES = [
        ('', ''),
        ('PC', 'PC'),
        ('PS1', 'PlayStation 1'),
        ('PS2', 'PlayStation 2'),
        ('PS3', 'PlayStation 3'),
        ('PS4', 'PlayStation 4'),
        ('PS5', 'PlayStation 5'),
        ('PSP', 'PlayStation Portable'),
        ('PSV', 'PlayStation Vita'),
        ('NES', 'Nintendo Entertainment System'),
        ('SNS', 'Super Nintendo Entertainment System'),
        ('N64', 'Nintendo 64'),
        ('NGC', 'Nintendo GameCube'),
        ('WII', 'Wii'),
        ('WIU', 'Wii U'),
        ('SW', 'Nintendo Switch'),
        ('GB', 'Game Boy'),
        ('GBC', 'Game Boy Color'),
        ('GBA', 'Game Boy Advance'),
        ('NDS', 'Nintendo DS'),
        ('3DS', 'Nintendo 3DS'),
        ('XBX', 'XBox'),
        ('360', 'XBox 360'),
        ('XBO', 'XBox One'),
        ('XBS', 'XBox Series'),
        ('IOS', 'Apple iOS'),
        ('AND', 'Android'),
    ]

    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    platform = models.CharField(max_length=3, choices=PLATFORM_CHOICES)
    owned = models.CharField(max_length=2, default='', choices=OWNED_CHOICES)

    class Meta:
        verbose_name_plural = "videogame details"

    def clean(self):
        if self.item.type != 'VG':
            raise ValidationError('Videogame details added to a non-videogame item')


class MovieDetails(models.Model):
    OWNED_CHOICES = [
        ('', ''),
        ('PH', 'Physical'),
        ('EB', 'Digital'),
        ('EB', 'Subscription'),
        ('NO', 'Not owned'),
    ]

    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    owned = models.CharField(max_length=2, default='', choices=OWNED_CHOICES)

    class Meta:
        verbose_name_plural = "movie details"

    def clean(self):
        if self.item.type != 'MV':
            raise ValidationError('Movie details added to a non-movie item')


class Tag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
