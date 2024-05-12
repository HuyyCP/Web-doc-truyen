from django.shortcuts import render
from manga.apis import mangaAPI
from chapter.apis import chapterAPI

class MangaView: 
    def getMangaBySlug(self, request, slug):
        return self.getMangaBySlugAndPage(request, slug, 1)

    def getMangaBySlugAndPage(self, request, slug, pageNum):
        manga = mangaAPI.getMangaBySlug(slug)
        limit = 20
        offset = (pageNum - 1) * limit
        chapters = chapterAPI.getChaptersByManga(manga.id, offset, limit)
        totalChapter = chapterAPI.getNumOfChapterByManga(manga.id)
        context = {
            'manga': manga,
            'chapters': chapters,
            'totalChapter': totalChapter,
            'pageNum': pageNum
        }
        return render(request, 'manga/manga_detail.html', context)
    
mangaView = MangaView()