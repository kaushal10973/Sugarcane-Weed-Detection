from ultralytics import YOLO
import os

# Load trained model
model_path = os.path.join("models", "weed_detection2", "weights", "best.pt")
model = YOLO(model_path)

# Predict on test images
results = model.predict(
    source="data/images/test",
    save=True,
    save_txt=True,
    project="output/output_images2"
)

print("Predictions saved in output/output_images")
