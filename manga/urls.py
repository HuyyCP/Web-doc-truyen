from django.urls import path
from manga.views import mangaView

urlpatterns = [
    path('upload', mangaView.uploadMangaView, name='uploadManga'),
    path('<slug>', mangaView.getMangaBySlug),
    path('<slug>/page-<pageNum>', mangaView.getMangaBySlugAndPage),
    path('<slug>/edit', mangaView.editManga, name='edit-manga'),
    path('<id>/delete', mangaView.deleteManga, name='delete-manga'),
]
