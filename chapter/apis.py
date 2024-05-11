from .models import Chapter
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class ChapterAPI:
    def getChaptersByManga(self, manga_id):
        data = Chapter.objects.filter(manga_id=manga_id).order_by('index')
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


chapterAPI = ChapterAPI()