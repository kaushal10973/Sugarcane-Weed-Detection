# Weed Detection in Sugarcane Fields using YOLOv8

## 📌 Overview
This project detects **weeds** in sugarcane fields using the YOLOv8 object detection model.  
It helps in early weed identification for better crop management.

---

## 📂 Project Structure
Sugarcane_Weed_Detection/
├── src/ # Training & prediction scripts
├── data/ # Dataset (images + labels)
├── models/ # Saved YOLOv8 weights
├── output/ # Prediction results
├── docs/ # Documentation
└── requirements.txt # Dependencies


---

## 📊 Dataset
Images labeled with weed bounding boxes only.
Labels are in YOLOv8 TXT format.

Directory structure:
data/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
└── dataset.yaml


---

## 🚀 Installation
```bash
git clone <repo_url>
cd Sugarcane_Weed_Detection
pip install -r requirements.txt


🏋️ Training

python src/train.py

🔍 Prediction

python src/predict.py

📈 Results
Target: >80% mAP
Output images with bounding boxes are saved in output/output_images/.