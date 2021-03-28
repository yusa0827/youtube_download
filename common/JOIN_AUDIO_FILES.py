import os
from pydub import AudioSegment
from common.YOUTUBE_DOWNLOAD import YOUTUBE_DOWNLOAD

class JOIN_AUDIO_FILES(YOUTUBE_DOWNLOAD):
    def __init__(self):
        super().__init__() 
        self.sounds = []

    def output_file_name(self, output_file_name):
        self.output_file_name = output_file_name

    def find_files(self):
        self.files = os.listdir(self.output_folder_path)

    def set_audio_file(self, file):
        return AudioSegment.from_file(file, "mp3")

    def set_audio_file_to_audio_file_temporarily(self):
        for file in self.files:
            file_path = self.output_folder_path + "/" + file
            self.sounds.append(self.set_audio_file(file_path))
        
        self.main_sound = self.sounds[0]
        for i in range(len(self.sounds) - 1):
            self.main_sound += self.sounds[i]

    def output_joined_audio_file(self):
        self.output_audio_file_path = self.output_folder_path + "/" + self.output_file_name
        self.main_sound.export(self.output_audio_file_path, format="mp3")

    def join_audio_file_to_audio_file(self):
        self.find_files()
        self.set_audio_file_to_audio_file_temporarily()
        self.output_joined_audio_file()
    
    def __del__(self):
        for file in self.files:
            file_path = self.output_folder_path + "/" + file        
            os.remove(file_path)

