from django.urls import path
from chapter.views import chapterView

urlpatterns = [
    path('chapter-<index>', chapterView.getChapterBySlugAndIndex),
    path('add-chapter', chapterView.addChapter, name='add-chapter'),
]