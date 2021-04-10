from common.GOOGLE_DRIVE_UPLOAD import GOOGLE_DRIVE_UPLOAD

def main():
    media_type = "mp3"
    folder_path = "media"
    urls       = [
        "https://www.youtube.com/watch?v=BjJbNr-CniM",
        "https://www.youtube.com/watch?v=xh83Z9ZpnkA"
    ]
    output_audio_integrator_file = "test.mp3"

    paramaters = {
        "media_type":media_type, 
        "folder_path":folder_path , 
        "url":urls,
        "output_audio_integrator_file":output_audio_integrator_file
    }

    youtube_dl = GOOGLE_DRIVE_UPLOAD()
    youtube_dl.set_parameter(paramaters)
    youtube_dl.donwload()

    if media_type == "mp3":
        youtube_dl.integrate_audio_file()
        youtube_dl.upload_file()

if __name__ == "__main__" :
    main()
