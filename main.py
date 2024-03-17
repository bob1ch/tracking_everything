from downloader import downloader_engine as d_eng
from yolo import yolo_tracking as model 






if __name__ == "__main__":
    d_eng.download_video("https://youtu.be/GnRQtA28BfY?si=8-_PZs_wWJU7HHPL")
    model.track()
