from ultralytics import YOLO

def track():
    model = YOLO('yolov8n.pt')
    results = model.track(source='./videos/test.mp4', show=True)
