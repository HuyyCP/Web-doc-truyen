from django.shortcuts import render
from manga.apis import mangaAPI
from chapter.apis import chapterAPI
from genre.apis import genreAPI
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import SearchForm
from django.views.generic import View
import json
from django.core import serializers

class MainView(View):
    def home_view(self, request):
        hotMangas = mangaAPI.getHotMangas()
        totalChapters = []
        for manga in hotMangas:
            totalChapters.append(chapterAPI.getNumOfChapterByManga(manga.id))
        context = {
            'mangas': hotMangas,
            'totalChapters': totalChapters,
        }
        return render(request, 'home.html', context)
    
    def manageView(self, request):
        mangas = mangaAPI.getMangaByUploader(request.user)
        totalChapters = []
        for manga in mangas:
            totalChapters.append(chapterAPI.getNumOfChapterByManga(manga.id))
        context = {
            'mangas': mangas,
            'totalChapters': totalChapters,
            # 'data': zip(mangas, totalChapters),
        }
        return render(request, 'manage.html', context)

    def searchView(self, request):
        genres = genreAPI.getAllGenres()
        if (request.method == 'POST'):
            data = json.loads(request.body)
            genresIncluded = data['genresIncluded']
            genresExcluded = data['genresExcluded']

            mangas = mangaAPI.getMangasByFilters(genresIncluded, genresExcluded)
            totalChapters = [chapterAPI.getNumOfChapterByManga(manga.id) for manga in mangas]


            mangas = serializers.serialize('json', mangas)
            response = {
                'mangas': mangas,
                'totalChapters': totalChapters,
            }

            return JsonResponse(response)
        elif (request.method == 'GET'):
            form = SearchForm()
            context = {
                'form': form,
                'genres': genres
            }
            return render(request, 'search.html', context)

    
mainView = MainView()