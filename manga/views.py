from django.shortcuts import render
from manga.apis import mangaAPI
from chapter.apis import chapterAPI

class MangaView: 
    def getMangaBySlug(self, request, slug):
        manga = mangaAPI.getMangaBySlug(slug)
        chapters = chapterAPI.getChaptersByManga(manga.id)
        context = {
            'manga': manga,
            'chapters': chapters
        }
        print(manga.avatarLink)
        return render(request, 'manga/manga_detail.html', context)
    
mangaView = MangaView()