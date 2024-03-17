from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"

def download_video(video_url, filename):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY, filename=filename)
    except:
        print("Failed to downlaod video")

    print("Video was downloaded successfully")
