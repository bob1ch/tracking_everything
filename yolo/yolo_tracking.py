from ultralytics import YOLO

def load_model():
    return YOLO('yolov8n.pt')


def track(video_name: str):
    model = YOLO('yolov8n.pt')
    results = model.track(source=f'./videos/{video_name}', show=True)
