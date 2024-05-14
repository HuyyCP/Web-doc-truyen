from django.urls import path
from chapter.views import chapterView

urlpatterns = [
    path('manga/<slug:slug>/chapter-<int:index>', chapterView.getChapterBySlugAndIndex),
    path('manga/<slug:slug>/add-chapter', chapterView.addChapter, name='add-chapter'),
]