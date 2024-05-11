from django.shortcuts import render
from manga.apis import mangaAPI


def home_view(request):
    hotMangas = mangaAPI.getHotMangas()
    context = {
        'mangas': hotMangas
    }
    return render(request, 'home.html', context)