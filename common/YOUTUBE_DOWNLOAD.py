import sys, os, subprocess

class YOUTUBE_DOWNLOAD:

    def __init__(self):
        self.media_type_mp3 = "youtube-dl -x --audio-format mp3 "
        self.media_type_mp4 = "youtube-dl -i -f mp4 --add-metadata "

    def set_parameter(self, paramaters):
        self.media_type         = paramaters["media_type"]
        self.output_folder_path = paramaters["folder_path"]
        self.urls               = paramaters["url"]
        self.set_output_folder_path()
        if self.media_type == "mp3":
            self.output_file_name   = paramaters["output_joined_audio_file"]

    def is_folder_made_if_not_exit(self):
        if not os.path.exists(self.output_folder_path):#ディレクトリがなかったら
            os.mkdir(self.output_folder_path)#作成したいフォルダ名を作成

    def set_output_folder_path(self):
        self.output_folder_path = self.output_folder_path + "_" + self.media_type
        self.is_folder_made_if_not_exit()
        self.output_folder_path_for_download = " -o ./{}/%(title)s.%(ext)s ".format(self.output_folder_path)

    def set_cmd(self, url):
        if self.media_type == "mp3":
            return self.media_type_mp3 + url + self.output_folder_path_for_download
        elif self.media_type == "mp4":
            return self.media_type_mp4 + url + self.output_folder_path_for_download
        else:
            print("No media type")
            sys.exit()

    def get_youtube_mp3(self, url):
        self.cmd = self.set_cmd(url)
        try:
            subprocess.check_call(self.cmd.split())
        except:
            print("error download")            
    
    def donwload(self):
        for url in self.urls:
            self.get_youtube_mp3(url)

