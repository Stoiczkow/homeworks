from django.shortcuts import render, redirect
from .forms import SearchMoviesForm
from django.contrib.auth.forms import UserCreationForm
from .models import Movie
# from django.contrib import messages
from rest_framework import viewsets
from .serializers import MovieSerializer

# 1. Widok na stronie głównej
def home_page(request):
    form = SearchMoviesForm()
    movies = Movie.objects.all().order_by("-release_date")[:8]

    return render(request, "home_page_cinema.html", {
        "form": form,
        "movies": movies
    })

# 2. Widok po wpisaniu filmu w wyszukiwarkę
def search_movies_results(request):
    form = SearchMoviesForm(request.GET)
    movie_result = Movie.objects.none()
    query = ""

    if form.is_valid():
        query = form.cleaned_data.get('name')
        if query:
            movie_result = Movie.objects.filter(title__icontains=query)
        
    return render(request, "search_results.html", {
        "movies": movie_result,
        "query": query
    })

# 3. Pełny repertuar kinowy
def show_all_movies(request):
    movies = Movie.objects.all().order_by('-release_date').prefetch_related('screenings')
    return render(request, "repertuar.html", {"movies": movies})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-release_date')
    serializer_class = MovieSerializer