from django.db import models

class Movie(models.Model):
    """Model movie"""
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    score = models.IntegerField()

 
