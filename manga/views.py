from django.shortcuts import render, redirect
from django.contrib import messages
from manga.apis import mangaAPI
from chapter.apis import chapterAPI
from manga.forms import UploadMangaForm, EditMangaForm
from django.views.generic import View

class MangaView(View): 
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
        return render(request, 'manga/manga_detail_remake.html', context)
    
    def uploadMangaView(self, request):
        if request.method == "POST":
            form = UploadMangaForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                avatar = form.cleaned_data['avatarInput']
                author = form.cleaned_data['author']
                genres = form.cleaned_data['genres']
                description = form.cleaned_data['description']
                uploader = request.user
                
                mangaAPI.createManga(title, avatar, author, genres, description, uploader)
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
        manga = mangaAPI.getMangaBySlug(slug)
        if request.method == "POST":
            form = EditMangaForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                newTitle = form.cleaned_data['title']
                newAvatar = form.cleaned_data['avatarInput']
                newGenres = form.cleaned_data['genres']
                newDesc = form.cleaned_data['description']
                mangaAPI.updateManga(manga, newTitle, newAvatar, newGenres, newDesc)
            else :
                print(form.errors)   
            return redirect('manage')
        else: 
            form = EditMangaForm(instance=manga)
            chapters = chapterAPI.getAllChaptersByManga(manga)
            context = {
                'form': form, 
                'manga': manga,
                'chapters': chapters
            }
            return render(request, 'manga/edit_manga.html', context)

    def deleteManga(self, request, id):
        mangaAPI.deleteManga(id)
        return redirect('manage')
     
mangaView = MangaView()