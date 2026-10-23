from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users", default="users/default.jpg")
    # Default is optional per the rubric; it also lets `createsuperuser` work.
    level = models.IntegerField(default=1, validators=[MinValueValidator(1)])
