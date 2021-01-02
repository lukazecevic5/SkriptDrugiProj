from django.db import models


class Movie(models.Model):
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content


class Review(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
