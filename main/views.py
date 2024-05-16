from django.shortcuts import render
from manga.apis import mangaAPI
from chapter.apis import chapterAPI

class MainView:
    def home_view(self, request):
        hotMangas = mangaAPI.getHotMangas()
        context = {
            'mangas': hotMangas
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
    
mainView = MainView()