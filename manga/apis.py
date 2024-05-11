from .models import Manga

class MangaAPI:

    def getHotMangas(self):
        data = Manga.objects.all()
        return data

    def getMangaBySlug(self, slug):
        data = Manga.objects.get(slug=slug)
        return data

mangaAPI = MangaAPI()
    
