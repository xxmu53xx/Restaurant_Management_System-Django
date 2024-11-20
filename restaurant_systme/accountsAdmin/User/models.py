# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=False)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username

