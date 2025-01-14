from django.db import models
from django.contrib.auth.models import AbstractUser
from movie_manager.movies.models import Movieinfo  # Adjust the import path as necessary

# Create your models here.
class User(AbstractUser):
    list = models.ManyToManyField(Movieinfo, blank=True, related_name='users')

    def __str__(self):
        return self.list