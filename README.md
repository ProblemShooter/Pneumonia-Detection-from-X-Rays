# Pneumonia Detection from X-Rays

![Project Banner](https://img.shields.io/badge/ML-Pneumonia%20Detection-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-orange)
![TensorFlow](https://img.shields.io/badge/ML-TensorFlow-red)
![Status](https://img.shields.io/badge/status-Experimental-yellow)

## Overview

This project is a complete end-to-end pneumonia detection system for chest X-ray images. It combines a deep learning model built with transfer learning, a Jupyter notebook training pipeline, and a Flask web application for real-time image upload and prediction.

The goal is to demonstrate how medical imaging classification can be deployed as a usable web interface, while keeping the workflow reproducible and easy to understand.

---

## 🚀 Key Features

- **Deep learning model** based on a custom VGG19 architecture
- **Transfer learning** with progressive fine-tuning
- **Web deployment** using Flask + Gunicorn
- **Image preprocessing** and prediction pipeline
- **Documentation** for model, deployment, and explanation
- **Production-ready** deployment configuration for Render

---

## 🧠 Model Architecture

The model uses a pre-trained `VGG19` base for feature extraction and a custom classification head:

```text
Input Image (224×224×3)
        ↓
VGG19 base (pre-trained on ImageNet)
        ↓
Flatten
        ↓
Dense(4608, relu)
        ↓
Dropout(0.2)
        ↓
Dense(1152, relu)
        ↓
Dense(2, softmax)
```

### Classes
- `0`: Normal
- `1`: Pneumonia

---

## 📁 Repository Structure

```text
PNEUMONIA_DETECTION/
├── Flask Application/               # Flask app, templates, static assets
│   ├── app.py                       # Prediction backend
│   ├── templates/                   # HTML views
│   ├── static/                      # CSS & JS files
│   └── uploads/                     # Uploaded x-rays
├── model_weights/                   # Saved model files (.h5)
├── Pneumonia Detection Using Deep Learning.ipynb
├── requirements.txt
├── README.md
├── deployment.md                    # Deployment instructions
├── explanation.md                   # Project explanation
├── runtime.txt                      # Render Python runtime pin
└── render.yaml                      # Render service config
```

---

## 🧩 Tech Stack

| Layer | Technology |
|------|------------|
| Web App | Flask, Jinja2, HTML, CSS, JavaScript |
| Model | TensorFlow, Keras, VGG19, Transfer Learning |
| Image Processing | OpenCV, Pillow, NumPy |
| Deployment | Render, Gunicorn, Runtime config |
| Data Visualization | Matplotlib, Seaborn |

---

## 📌 What is included

- `Pneumonia Detection Using Deep Learning.ipynb` — training pipeline, augmentation, evaluation, and model saving
- `Flask Application/app.py` — backend server, image upload, preprocessing, and prediction logic
- `requirements.txt` — exact Python packages used in the project
- `deployment.md` — step-by-step deployment instructions
- `explanation.md` — detailed project explanation for reviewers
- `runtime.txt` and `render.yaml` — Render-specific runtime and service configuration

---

## 🛠️ How it Works

### Training pipeline
1. Load the chest X-ray dataset
2. Apply data augmentation and rescaling
3. Train the custom VGG19-based model
4. Save weights to `model_weights/`

### Web app pipeline
1. User uploads an X-ray image to the Flask UI
2. Image is read and converted to RGB
3. Image is resized to `224×224`
4. Image is normalized and passed to the model
5. Model returns `Normal` or `Pneumonia`

---

## 💡 Usage

### Local setup

```bash
git clone https://github.com/ProblemShooter/Pneumonia-Detection-from-X-Rays.git
cd PNEUMONIA_DETECTION
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd "Flask Application"
python app.py
```

Then open the browser at:

```text
http://127.0.0.1:5000
```

### Render deployment

1. Push the repo to GitHub
2. Connect the repo in Render
3. Set the start command to:

```bash
gunicorn -w 4 -b 0.0.0.0:$PORT "Flask Application.app:app"
```

4. Ensure the Python runtime is pinned to `3.13.13` or `3.11.4`
5. Deploy and verify the web app

---

## 📊 Model Notes

- Uses **softmax** for binary classification
- Works with **color RGB images** converted from OpenCV BGR input
- Saves model weights in the `model_weights` folder
- Deployment uses the best saved model weights for prediction

---

## 🧪 Testing

Test the app by uploading X-ray images on the web UI and verifying the prediction result. For best results, use real chest X-ray images or sample dataset images from the training data.

---

## 🎯 Why this project matters

Pneumonia detection from medical scans is an important real-world application of deep learning. This project demonstrates:

- how to build a medical imaging classifier
- how to apply transfer learning to a challenging dataset
- how to deploy a working model with a real web frontend

---

## 📚 References

- [TensorFlow transfer learning docs](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [Flask quickstart](https://flask.palletsprojects.com/)
- [Render docs](https://render.com/docs)

---

## ⚠️ Notes

- The repository should not include large model files or raw dataset files in GitHub.
- Use `model_weights/.gitkeep` to preserve the directory structure while ignoring weight files.
- Use the same `requirements.txt` and `runtime.txt` versions for deployment consistency.
