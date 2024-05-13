from .models import Manga
from django.utils.text import slugify
from utils.handleDrive import create_folder_in_drive, upload_file_to_drive
from environ import Env
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
import tempfile
from django.contrib.auth.models import User
import os

env = Env()
env.read_env('.env')

class MangaAPI:

    def getHotMangas(self):
        data = Manga.objects.all()
        return data

    def getMangaBySlug(self, slug):
        data = Manga.objects.get(slug=slug)
        return data
    
    def createManga(self, title, avatar, author, genres, description):
        slug = slugify(title)
        if isinstance(avatar, InMemoryUploadedFile):
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(avatar.read())
                avatar_path = temp_file.name
        elif isinstance(avatar, TemporaryUploadedFile):
            avatar_path = avatar.temporary_file_path()
        
        manga_folder_id = create_folder_in_drive(slug, env('ROOT_FOLDER_ID'))
        avatar_id = upload_file_to_drive(avatar_path, manga_folder_id, alter_filename='avatar')
        avatar_link =  f"https://drive.google.com/thumbnail?id={avatar_id}&sz=w1000"
        manga = Manga.objects.create(
            title=title, 
            slug=slug, 
            description=description, 
            avatarLink=avatar_link, 
            idDrive=manga_folder_id, 
            uploader=User.objects.get(id='1'), 
            author=author, 
        )
        manga.genres.set(genres)
        manga.save()
        print(manga_folder_id)  

mangaAPI = MangaAPI()
    
