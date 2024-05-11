from django.urls import path
from manga.views import mangaView

urlpatterns = [
    path('<slug:slug>', mangaView.getMangaBySlug, name='manga_detail')
]
