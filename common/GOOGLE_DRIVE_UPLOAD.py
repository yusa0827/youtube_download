from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from common.MEDIA_INTEGRATOR import MEDIA_INTEGRATOR
import os, sys

class GOOGLE_DRIVE_UPLOAD(MEDIA_INTEGRATOR):
    def __init__(self):
        super().__init__() 
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        self.drive = GoogleDrive(gauth)

    def set_upload_file(self):
        self.upload_file_to_google_drive = self.drive.CreateFile(
            {'title': self.output_file_name, 'mimeType': 'audio/mp3'})
        try:
            if not os.path.exists(self.output_file_name):
                print("not exist output_file_name") 
            self.upload_file_to_google_drive.SetContentFile(self.output_file_name)
        except:
            print("error upload", self.output_file_name)             
            sys.exit()
            
    def upload_file(self):
        self.set_upload_file()
        try:
            self.upload_file_to_google_drive.Upload()
            print("upload file")
        except:
            print("error upload file")

            