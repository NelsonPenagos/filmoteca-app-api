from .models import User, Movie
from .serializers import UserSerializer, MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list(request):
    """List all movies or Create new movie"""
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    """Retrive, update or delete movie"""

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movie_recommendation(request):
    """recommendation movies"""

    try:
        movie = Movie.objects.filter(score__gt = 3)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_name(request, name):
    """search movies by name"""

    try:
        movie = Movie.objects.filter(name__contains = name)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_genre(request, genre):
    """search movies by genre"""

    try:
        movie = Movie.objects.filter(genre__contains = genre)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_director(request, director):
    """search movies by director"""

    try:
        movie = Movie.objects.filter(director__contains = director)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)


