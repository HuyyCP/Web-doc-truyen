from django.shortcuts import render
from chapter.apis import chapterAPI
from manga.apis import mangaAPI


class ChapterView:
    def getChapterBySlugAndIndex(self, request, slug, index):
        manga = mangaAPI.getMangaBySlug(slug)
        chapter = chapterAPI.getChapterByIndex(manga.id, index)
        context = {
            'manga': manga,
            'chapter': chapter 
        }
        return render(request, 'chapter/chapter.html', context)

chapterView = ChapterView()