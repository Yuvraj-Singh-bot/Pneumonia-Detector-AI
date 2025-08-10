# 🩺 Pneumonia Detector AI

This project is an **AI-powered pneumonia detection system** that uses **DenseNet101** for classification and a **Streamlit** web application for deployment.

---

## 📂 Dataset

We used the **Chest X-Ray Pneumonia** dataset from Kaggle:  
[🔗 Kaggle Dataset Link](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

The dataset contains chest X-ray images categorized into **Normal** and **Pneumonia** cases.

---

## 🧠 Model

- **Architecture:** DenseNet101 (Pre-trained on ImageNet, fine-tuned for pneumonia classification)
- **Framework:** TensorFlow / Keras
- **Output:** Binary classification — `Pneumonia` or `Normal`

**Why DenseNet101?**  
DenseNet models are known for:
- Efficient parameter usage
- Better gradient flow during training
- Strong performance on medical image classification tasks

---

## 🌐 Deployment

The project is deployed as a **Streamlit** app for easy interaction.  
Users can upload a chest X-ray image and get an instant prediction.

---

## ▶️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Yuvraj-Singh-bot/Pneumonia-Detector-AI.git
cd Pneumonia-Detector-AI
python -m venv chest
chest\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
