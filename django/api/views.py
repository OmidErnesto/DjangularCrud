from rest_framework.response import Response
from api.models import Movie
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import MovieMiniSerializer, MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)
