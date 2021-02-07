from django.views.generic import ListView, DetailView

from .models import Movie


class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    context_object_name = 'movies_list'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
