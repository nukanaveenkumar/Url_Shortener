# shortener/models.py
from django.db import models

class URL(models.Model):
    original = models.URLField()
    shortened = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.original
