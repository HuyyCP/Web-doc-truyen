from django.urls import path
from manga.views import mangaView

urlpatterns = [
    path('upload', mangaView.uploadMangaView, name='uploadManga'),
    path('<slug:slug>', mangaView.getMangaBySlug),
    path('<slug:slug>/page-<int:pageNum>', mangaView.getMangaBySlugAndPage),
]
