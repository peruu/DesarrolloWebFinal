from django.db import models

# Create your models here.

class Genre(models.Model):
    adventure = models.BooleanField()
    art = models.BooleanField()
    biography = models.BooleanField()
    fiction = models.BooleanField()
    fantasy = models.BooleanField()
    history = models.BooleanField()
    horror = models.BooleanField()
    mistery = models.BooleanField()
    miythology = models.BooleanField()
    poetry = models.BooleanField()
    romance = models.BooleanField()
    science = models.BooleanField()
    superhero = models.BooleanField()
    thriller = models.BooleanField()
    tragedy = models.BooleanField()
    western = models.BooleanField()
    