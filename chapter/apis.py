from .models import Chapter
from django.db.models import Max
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from utils.handleDrive import create_folder_in_drive, upload_file_to_drive, delete_file_or_folder
import tempfile


class ChapterAPI:
    def getAllChaptersByManga(self, manga):
        data = Chapter.objects.filter(manga=manga)
        return data

    def getChaptersByManga(self, manga_id, offset, limit):
        data = Chapter.objects.filter(manga_id=manga_id).order_by('index')[offset:offset+limit]
        return data
    
    def getChapterByIndex(self, manga_id, index): 
        chapter = Chapter.objects.get(manga_id=manga_id,index=index)
        credentials = Credentials.from_service_account_file('credentials.json')
        drive_service = build('drive', 'v3', credentials=credentials)

        results = drive_service.files().list(q=f"'{chapter.idDrive}' in parents", fields="files(name, id)").execute()
        files = results.get('files', [])
        if not files:
            print('No files found.')
        else:
            files = sorted(files, key=lambda file: int(file['name'][:file['name'].index('.')]))
            for file in files:
                file['link'] = f"https://drive.google.com/thumbnail?id={file['id']}&sz=w1000"
        chapter = {
            'info': chapter,
            'pages': files
        }
        return chapter

    def getNumOfChapterByManga(self, manga_id):
        data = Chapter.objects.filter(manga_id=manga_id).count()
        return data
    
    def addChapter(self, title, files, manga):
        max_index = Chapter.objects.filter(manga=manga).aggregate(Max('index'))
        chapter_index = max_index['index__max'] + 1 if max_index['index__max'] is not None else 1
        chapter_folder_id = create_folder_in_drive(str(chapter_index), manga.idDrive)
        for index, file in enumerate(files):
            if isinstance(file, InMemoryUploadedFile):
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(file.read())
                    file_path = temp_file.name
            elif isinstance(file, TemporaryUploadedFile):
                file_path = file.temporary_file_path()

            upload_file_to_drive(file_path, chapter_folder_id, str(index))
        
        chapter = Chapter.objects.create(
            title=title,
            index=chapter_index,
            manga=manga,
            idDrive=chapter_folder_id
        )
        chapter.save()

    def deleteChapter(self, chapter_id):
        chapter = Chapter.objects.get(id=chapter_id)
        delete_file_or_folder(chapter.idDrive)
        chapter.delete()
        
chapterAPI = ChapterAPI()