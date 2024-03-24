import uvicorn
from fastapi import FastAPI
from downloader import downloader_engine as d_eng
from yolo import yolo_tracking

app = FastAPI()
model = None

@app.on_event("startup")
def startup_event():
    global model
    model = yolo_tracking.load_model()

@app.get('/track')
def result_tracking(video_name: str = 'test.mp4'):
    yolo_tracking.track(video_name)

@app.get('/')
async def test():
    return {"hello": "world"}

@app.get('/download')
def download(url: str = "https://youtu.be/GnRQtA28BfY?si=8-_PZs_wWJU7HHPL", 
             name: str = "test.mp4"):
    d_eng.download_video(url, name)


uvicorn.run(app, host="0.0.0.0", port=8000)
