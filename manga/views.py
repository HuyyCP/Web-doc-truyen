from django.shortcuts import render, redirect
from django.contrib import messages
from manga.apis import mangaAPI
from chapter.apis import chapterAPI
from manga.forms import UploadMangaForm

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
    
    def uploadMangaView(self, request):
        if request.method == "POST":
            form = UploadMangaForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                title = form.cleaned_data['title']
                avatar = form.cleaned_data['avatarInput']
                author = form.cleaned_data['author']
                genres = form.cleaned_data['genres']
                description= form.cleaned_data['description']
                
                mangaAPI.createManga(title, avatar, author, genres, description)
            else: 
                print(form.errors)
            return redirect('manage')
        else:
            form = UploadMangaForm()
            context = {
                'form': form
            }
            return render(request, 'manga/upload.html', context)
    
    def editManga(self, request, slug):
        print()

    def deleteManga(self, request, id):
        print()
     
mangaView = MangaView()