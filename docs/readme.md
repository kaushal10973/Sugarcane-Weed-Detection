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

## 📈 Results
P (Precision) = 89.2%
R (Recall) = 87.4%
mAP@0.5 = 85.1%

## Output
Output images with bounding boxes are saved in output/output_images/.

# Dataset
Source: Roboflow dataset
link: https://universe.roboflow.com/abhishek-trvj4/sugarcane-weed/dataset/1

## 🚀 Installation
```bash
git clone https://github.com/kaushal10973/Sugarcane-Weed-Detection
cd Sugarcane_Weed_Detection

# Create virtual environment (recommended)
python -m venv .venv
# Activate environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

#Training
python src/train.py

#Prediction
python src/predict.py
