from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from common.JOIN_AUDIO_FILES import JOIN_AUDIO_FILES

class GOOGLE_DRIVE_UPLOAD(JOIN_AUDIO_FILES):
    def __init__(self):
        super().__init__() 
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        self.drive = GoogleDrive(gauth)

    def set_upload_file(self):
        self.f = self.drive.CreateFile(
            {'title': "無題のフォルダ/" + self.output_file_name, 'mimeType': 'audio/mp3'})
        print(self.output_folder_path + "/" + self.output_file_name)
        self.f.SetContentFile(self.output_folder_path + "/" +self.output_file_name)

    def upload_file(self):
        self.set_upload_file()
        try:
            self.f.Upload()
            print("upload file")
        except:
            print("error upload file")

            