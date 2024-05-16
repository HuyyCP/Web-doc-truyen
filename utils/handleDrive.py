from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload
import os

credentials = Credentials.from_service_account_file('credentials.json')
service = build('drive', 'v3', credentials=credentials)

def check_file_or_folder_exists_in_folder(name, folder_id, is_folder=False):
    
    query = f"name='{name}' and '{folder_id}' in parents"
    if is_folder:
        query += " and mimeType='application/vnd.google-apps.folder'"

    results = service.files().list(
        q=query,
        spaces='drive',
        fields='files(id)',
        pageToken=None
    ).execute()

    items = results.get('files', [])
    if len(items) > 0:
        print(f"{name} exists in the folder.")
        return True
    else:
        print(f"{name} does not exist in the folder.")
        return False

def create_folder_in_drive(folder_name, parent_folder_id=None):
    if not check_file_or_folder_exists_in_folder(folder_name, parent_folder_id, is_folder=True):
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_folder_id:
            folder_metadata['parents'] = [parent_folder_id]

        created_folder = service.files().create(
            body=folder_metadata,
            fields='id'
        ).execute()

        folder_id = created_folder.get('id')
        print('Folder created successfully. Folder ID:', folder_id)
        return folder_id

def upload_file_to_drive(file_path, folder_id=None, alter_filename=None):
    file_name = alter_filename if alter_filename else file_path.split('\\')[-1]
    file_metadata = {'name': f"{file_name}.jpg"}
    if folder_id:
        file_metadata['parents'] = [folder_id]
        
    media = MediaFileUpload(file_path)
    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    print('File uploaded successfully. File ID:', uploaded_file.get('id'))
    return uploaded_file.get('id')
