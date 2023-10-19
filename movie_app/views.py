from .models import MovieList
from rest_framework import viewsets
from .serializers import MovieListSerializer


# Create your views here.
class MovieListViewSet(viewsets.ModelViewSet):
    queryset = MovieList.objects.all().order_by("-title")
    serializer_class = MovieListSerializer
