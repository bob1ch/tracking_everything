from downloader import downloader_engine as d_eng
from yolo import yolo_tracking as model 
from api import engine_api



if __name__ == "__main__":
    engine_api
    d_eng.download_video("https://youtu.be/GnRQtA28BfY?si=8-_PZs_wWJU7HHPL", 'test.mp4')
    #model.track()
