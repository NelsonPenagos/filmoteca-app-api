from rest_framework import serializers
from .models import User, Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('user_id', 'email', 'password', 'first_name', 'last_name')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ('movie_id', 'name', 'genre', 'director', 'score')