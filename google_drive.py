from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload_file_to_drive(folder_id, file_path):
    creds = Credentials(
        token=os.environ['ACCESS_TOKEN'], 
        refresh_token=os.environ['REFRESH_TOKEN'], 
        client_id=os.environ['CLIENT_ID'], 
        client_secret=os.environ['CLIENT_SECRET'], 
        token_uri='https://oauth2.googleapis.com/token'
    )
    drive_service = build('drive', 'v3', credentials=creds)
    filename = os.path.basename(file_path)
    file_metadata = {
        'name': filename,
        'parents': [folder_id],
    }
    media = MediaFileUpload(file_path, mimetype='text/csv')
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(file.get("id"))
    return file.get('id')
