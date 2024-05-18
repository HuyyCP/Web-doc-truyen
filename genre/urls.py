from django.urls import path
from genre.views import genreView

urlpatterns = [
    path("all", genreView.getAllGenres, name='genre'),
    path("<slug>", genreView.getMangasByGenre, name='genre'),
]