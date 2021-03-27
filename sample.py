from common.JOIN_AUDIO_FILES import JOIN_AUDIO_FILES

def main():
    media_type = "mp3"
    folder_path = "media"
    urls       = [
        "https://www.youtube.com/watch?v=BjJbNr-CniM",
        "https://www.youtube.com/watch?v=xh83Z9ZpnkA"
    ]
    output_joined_audio_file = "output.mp3"

    url_folderpath_paramater = {
        "media_type":media_type, 
        "folder_path":folder_path , 
        "url":urls,
        "output_joined_audio_file":output_joined_audio_file
    }

    youtube_dl = JOIN_AUDIO_FILES()
    youtube_dl.set_parameter(url_folderpath_paramater)
    youtube_dl.donwload()

    if media_type == "mp3":
        youtube_dl.join_audio_file_to_audio_file()

if __name__ == "__main__" :
    main()
