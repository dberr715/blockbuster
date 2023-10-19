from .models import MovieList
from rest_framework import serializers


class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieList
        fields = ["title", "lead_roll", "director", "description"]
