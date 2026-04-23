# ⛑️ Helmet & Safety Vest Detector

![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Computer%20Vision-green?style=for-the-badge)

<img width="350" alt="cvimg2" src="https://github.com/user-attachments/assets/0618ef7b-05df-4c86-86f8-3e09287aec17" />
<img width="350" alt="cvimg1" src="https://github.com/user-attachments/assets/25ca8cc5-961a-4ed9-9b1e-6848ac3bf43e" />


> A real-time deep learning system that detects whether workers are wearing helmets and safety vests — built for industrial safety and compliance monitoring.

---

## 🚀 Live Demo

🔗 **Try it here:** [https://helmet-detector-anvctblqdfr9ah9k72gkx4.streamlit.app/]

Upload a photo or use your camera to instantly check for safety equipment compliance!

---

## 📌 Project Idea

In industrial worksites, ensuring workers wear proper safety equipment (helmets and vests) is critical. This project uses **YOLOv8** — a state-of-the-art deep learning model — to automatically detect:

| Class | Description |
|-------|-------------|
| ⛑️ **Helmet** | Worker is wearing a safety helmet |
| 🦺 **Vest** | Worker is wearing a safety vest |
| 👤 **Head** | Head detected without helmet (violation!) |

---

## 🧠 How It Works (Deep Learning)

```
Input Image/Camera Feed
        ↓
YOLOv8s Neural Network (11M parameters)
  ├── Backbone: CSPDarknet (feature extraction)
  ├── Neck: FPN+PAN (multi-scale features)
  └── Head: Detection (bounding box + class)
        ↓
Output: Bounding boxes + Labels + Confidence scores
```

The model **learns automatically** from 23,000+ labeled images — no handcrafted rules, pure deep learning.

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **mAP@50** | **88.4%** 🔥 |
| **Precision** | 86.9% |
| **Recall** | 84.0% |
| **mAP@50-95** | 54.1% |

Training curves show consistent improvement with **no overfitting**:

> *(Add your results.png image here)*

---

## 🗂️ Dataset

- **23,673 images** from multiple sources
- Split: 78% train / 11% test / 11% validation
- Images resized to **640×640 pixels**
- Annotations in **YOLO format**
- Sources: Harvard Dataverse, Roboflow, Kaggle

---

## 🛠️ Tech Stack

- **YOLOv8** (Ultralytics) — Object detection model
- **Python** — Core language
- **Streamlit** — Web app interface
- **OpenCV** — Image processing
- **Google Colab** — Training environment (Tesla T4 GPU)

---

## 📁 Project Structure

```
helmet-detector/
├── app.py              # Streamlit web application
├── best.pt             # Trained YOLOv8 model weights
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/helmet-detector.git
cd helmet-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🖼️ Sample Results

> *(Add sample detection images here — drag and drop into GitHub)*

---

## 🏭 Real-World Application

This system can be deployed in:
- 🏗️ **Construction sites** — Monitor workers in real-time
- 🏭 **Factories** — Automated compliance checking
- 🎥 **CCTV systems** — 24/7 safety monitoring
- 📱 **Mobile inspections** — On-site safety audits

---

## 👩‍💻 Author

Built as a Computer Vision course project.

---

*Powered by YOLOv8 + Streamlit*
