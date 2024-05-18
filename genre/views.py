from django.shortcuts import render
from django.views.generic import View
from genre.apis import genreAPI
from manga.apis import mangaAPI
from chapter.apis import chapterAPI
from django.utils.text import slugify
import json
from django.http import JsonResponse
from django.core import serializers

class GenreView(View): 

    def getAllGenres(self, request): 
        genres = genreAPI.getAllGenres()
        genres = serializers.serialize('json', genres)
        context = {
            'genres': genres
        }

        return JsonResponse(context)

    def getMangasByGenre(self, request, slug):
        slug = slug
        genre = genreAPI.getGenreBySlug(slug)
        mangas = mangaAPI.getMangasByFilters(str(genre.id), '')
        totalChapters = [chapterAPI.getNumOfChapterByManga(manga.id) for manga in mangas]
        
        context = {
            'mangas': mangas,
            'genre': genre,
            'totalChapters': totalChapters,
        }
        return render(request, 'genre/genre.html', context)


genreView = GenreView()