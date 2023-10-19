from django.db import models


# Create your models here.
class MovieList(models.Model):
    title = models.CharField(max_length=100)
    lead_roll = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.CharField()

    def __str__(self):
        return self.title
