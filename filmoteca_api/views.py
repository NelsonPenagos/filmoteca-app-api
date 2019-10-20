from .models import User, Movie
from .serializers import UserSerializer, MovieSerializer
from rest_framework import generics

class MovieListView(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer

