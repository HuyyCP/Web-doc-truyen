from django.shortcuts import render, redirect
from chapter.apis import chapterAPI
from manga.apis import mangaAPI
from chapter.forms import AddChapterForm
from django.views.generic import View

class ChapterView(View):
    def getChapterBySlugAndIndex(self, request, slug, index):
        manga = mangaAPI.getMangaBySlug(slug)
        chapter = chapterAPI.getChapterByIndex(manga.id, index)
        totalChapters = chapterAPI.getNumOfChapterByManga(manga.id)
        context = {
            'manga': manga,
            'chapter': chapter,
            'totalChapters': totalChapters
        }
        return render(request, 'chapter/chapter.html', context)
    
    def addChapter(self, request, slug):
        manga = mangaAPI.getMangaBySlug(slug)
        if request.method == 'POST':
            form = AddChapterForm(request.POST, request.FILES)
            if form.is_valid():
                print(form.cleaned_data)
                title = form.cleaned_data['title']
                files = request.FILES.getlist('files[]')
                print(files)
                chapterAPI.addChapter(title, files, manga)
            else:
                print(form.errors)
            
            return redirect('manage')
        else :
            form = AddChapterForm()
            context = {
                "manga": manga,
                'form': form
            }
            return render(request, 'chapter/add-chapter.html', context)

    def deleteChapter(self, request, slug, id):
        chapterAPI.deleteChapter(id)
        return redirect('edit-manga', slug=slug)
    
chapterView = ChapterView()