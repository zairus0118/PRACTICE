from django.core.validators import MinValueValidator
from django.db import models


class Pokemon(models.Model):
    TYPE_CHOICES = [
        ("water", "Water"),
        ("fire", "Fire"),
        ("wind", "Wind"),
        ("light", "Light"),
        ("darkness", "Darkness"),
        ("lightning", "Lightning"),
        ("rock", "Rock"),
        ("nature", "Nature"),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to="pokemons/avatars/", default="pokemons/avatars/profile default.jpg"
    )
    background = models.ImageField(
        upload_to="pokemons/background/", default="pokemons/background/bg default.png"
    )
    level = models.IntegerField(validators=[MinValueValidator(1)])
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    health = models.IntegerField(validators=[MinValueValidator(100)])
    attack = models.IntegerField(validators=[MinValueValidator(10)])
    defense = models.IntegerField(validators=[MinValueValidator(5)])
    speed = models.IntegerField(validators=[MinValueValidator(15)])

    def __str__(self):
        return self.name
