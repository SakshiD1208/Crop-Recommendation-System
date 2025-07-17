# 🌾 Crop Recommendation System using Machine Learning

## 📋 Overview
The **Crop Recommendation System** is a Django-based web application that predicts the most suitable crop for farming based on soil nutrients and environmental conditions.  
It leverages a trained machine learning model to make accurate predictions and provides an easy-to-use web interface for users.

---

## 🚀 Features
- ✔️ Clean, user-friendly web interface
- ✔️ Takes user input for key agricultural factors:
  - Nitrogen (N)
  - Phosphorous (P)
  - Potassium (K)
  - Temperature (°C)
  - Humidity (%)
  - pH
  - Rainfall (mm)
- ✔️ Real-time crop prediction using a trained Gradient Boosting Classifier model
- ✔️ Input scaling and label encoding for optimized predictions

---

## 🖥️ Tech Stack
- **Frontend:** HTML, CSS (Bootstrap)
- **Backend:** Python (Django Framework)
- **ML Libraries:** scikit-learn, pandas, pickle
- **Deployment:** Django Development Server (localhost)

---

## 📂 Project Structure
```
Crop Recommendation System/
├── crop_recommendation/
│   ├── predictor/
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── predictor/
│   │   │       ├── form.html
│   │   │       └── result.html
│   ├── crop_recommendation/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
├── models/
│   ├── model_gbc.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Used
- **Crop Recommendation Dataset**
- Source: [Kaggle Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download)
- Contains agricultural data with multiple features and crop labels used for model training.

---

## 🛠️ How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Crop-Recommendation-System.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd Crop Recommendation System
   ```

3. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Django Server**
   ```bash
   cd crop_recommendation
   python manage.py runserver
   ```

6. **Access the App**
   Open `http://127.0.0.1:8000/` in your browser.
