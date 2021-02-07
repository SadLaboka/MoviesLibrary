from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm


class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    context_object_name = 'movies_list'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
