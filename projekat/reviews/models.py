from django.db import models
from . import ranges
from django.contrib.auth.models import User


class Movie(models.Model):
    content = models.CharField(max_length=64)
    year = ranges.IntegerRangeField(min_value=1900, max_value=2100)

    def __str__(self):
        return self.content + '(' + str(self.year) + ')'


class Review(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
