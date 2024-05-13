from django.shortcuts import render
from manga.apis import mangaAPI


class MainView:
    def home_view(self, request):
        hotMangas = mangaAPI.getHotMangas()
        context = {
            'mangas': hotMangas
        }
        return render(request, 'home.html', context)
    
    def manageView(self, request):
        mangas = mangaAPI.getMangaByUploader(request.user)
        context = {
            'mangas': mangas
        }
        return render(request, 'manage.html', context)
    
mainView = MainView()