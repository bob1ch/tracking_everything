from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "../videos"

def download_video(video_url):
    video = YouTube('https://www.youtube.com/watch?v=X-ANZ8ba8jU')
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
    except:
        print("Failed to downlaod video")

    print("Video was downloaded successfully")
