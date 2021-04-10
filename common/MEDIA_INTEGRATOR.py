import sys, os, subprocess
from common.YOUTUBE_DOWNLOAD import YOUTUBE_DOWNLOAD

class MEDIA_INTEGRATOR(YOUTUBE_DOWNLOAD):
    def __init__(self):
        super().__init__() 
        
    def integrate_audio_file(self):
        cmd = "copy /b {}\*.mp3 {}".format(self.output_folder_path, self.output_file_name)
        print(cmd)
        try:
            subprocess.check_call(cmd, shell=True)
        except:
            print("error download") 

    def find_files(self):
        return os.listdir(self.output_folder_path)

    def __del__(self):
        for file in self.find_files():
            file_path = self.output_folder_path + "/" + file        
            os.remove(file_path)
    