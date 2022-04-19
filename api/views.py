from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_update(self, serializer):
        movie_instance = serializer.instance
        request = self.request
        serializer.save(**request.data)
        return Response(status=status.HTTP_200_OK)