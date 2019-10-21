from rest_framework import serializers
from filmoteca_api.models.movie_models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """MovieSerializer"""
    class Meta:
      model = Movie
      fields = ('movie_id', 'name', 'genre', 'director', 'score')