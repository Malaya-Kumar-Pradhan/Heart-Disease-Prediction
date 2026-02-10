# Heart Disease Prediction System

A full-stack Machine Learning web application designed to predict the likelihood of heart disease based on clinical patient data. This project demonstrates a complete end-to-end pipeline from data preprocessing and model training to API deployment.

### 🚀 [View Live App on Render](https://heart-disease-prediction-nu5b.onrender.com)
---

## 🚀 Features
* **Interactive Web Interface:** Clean, grid-based form for inputting patient data.
* **Real-time Inference:** Fast predictions using a serialized Scikit-Learn model.
* **Robust Preprocessing:** Custom pipeline handling IQR outlier clipping, Power Transformations, and Feature Scaling.
* **Production Ready:** Configured for deployment via FastAPI and Uvicorn.

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **Framework:** FastAPI
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend:** HTML5, CSS3, Jinja2
* **Server:** **Uvicorn** (ASGI Production Server)
* **Deployment:** **Render** (Cloud Hosting Platform)

## 📂 Project Structure
```text
.
├── main.py              # FastAPI application & API routes
├── model.pkl            # Trained Scikit-Learn model (Pickle format)
├── minMaxscaler.pkl          # Scaler for 'resting bp s'
├── cholesterol.pkl          # Scaler for 'cholesterol'
├── maxHeartRate.pkl          # Scaler for 'max heart rate'
├── static/
│   └── style.css        # Custom CSS for the UI
├── templates/
│   └── index.html       # Jinja2 HTML template
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## 📊 Methodology & Data Preprocessing
To ensure high model accuracy and stability, the following transformations were applied to the raw input:
* **Feature Renaming:** Form inputs are mapped to the specific feature names seen during model training (e.g., trestbps → resting bp s).
* **Outlier Clipping:** The Interquartile Range (IQR) method was used to cap extreme values in clinical features.
* **Mathematical Transformations:** A Power Transformation ($x^{0.2}$) was applied to the oldpeak feature to reduce distribution skewness.
* **Standardization:** Numeric features were normalized using StandardScaler to ensure all features contribute equally to the prediction.

## 💻 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.13 or more installed on your system. You can verify your version by running:
python --version

### 2. Clone the Repository
git clone https://github.com/your-username/Heart-Disease-Prediction.git

cd heart-disease-predictor

### 3. Set Up Virtual Environment
# Windows
python -m venv venv

.\venv\Scripts\activate

# Mac/Linux
python3.12 -m venv venv

source venv/bin/activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Run the Application
uvicorn main:app --reload

## 🌍 Deployment on Render

This project is already deployed and running live on **Render**. Below is the configuration used to host the FastAPI application:

### 1. Web Service Configuration
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 2. Environment Variables
To ensure the application uses the correct Python version and handles the serialized models correctly, the following environment variable was configured:
- **PYTHON_VERSION:** `3.13+`

### 3. Deployment Flow
Every time code is pushed to the `main` branch of this GitHub repository, Render automatically:
* **Pulls the latest code.**
* **Re-installs dependencies from `requirements.txt`.**
* **Restarts the Uvicorn server to apply changes.**
