from django.contrib import admin

from . import models

admin.site.register(models.Settings)
admin.site.register(models.Item)
admin.site.register(models.Tag)
admin.site.register(models.BookDetails)
admin.site.register(models.MovieDetails)
admin.site.register(models.VideogameDetails)
