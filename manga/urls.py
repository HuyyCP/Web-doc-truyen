from django.urls import path
from manga.views import mangaView

urlpatterns = [
    path('<slug:slug>', mangaView.getMangaBySlug, name='manga_detail'),
    path('<slug:slug>/page-<int:pageNum>', mangaView.getMangaBySlugAndPage, name='manga_page'),
]
