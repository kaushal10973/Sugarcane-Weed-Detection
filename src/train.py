from ultralytics import YOLO
import os

# Paths
DATASET_CONFIG = os.path.join("data", "dataset.yaml")
MODEL_SAVE_PATH = os.path.join("models")

# Create models folder if not exists
os.makedirs(MODEL_SAVE_PATH, exist_ok=True)

# Load YOLOv8 model (pre-trained COCO weights)
model = YOLO("yolov8s.pt")  # yolov8n = nano, yolov8s = small, yolov8m = medium

# Train model
model.train(
    data=DATASET_CONFIG,
    epochs=2,
    imgsz=640,
    batch=16,
    name="weed_detection",
    project=MODEL_SAVE_PATH,
)

print("Training complete. Best model saved in:", MODEL_SAVE_PATH)
