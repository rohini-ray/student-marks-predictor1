# 🎯 Student Marks Predictor

A web application designed to predict a student's final marks based on multiple features: study hours, attendance rate, previous scores, and sleep hours. The project features a Flask backend serving a trained Machine Learning model and a clean, user-friendly HTML/CSS/JavaScript frontend.

---

## 📁 Project Directory Structure

Here is the updated professional structure for this project:

```text
student-marks-predictor1/
│
├── backend/                   # Python Flask API & Machine Learning files
│   ├── models/                # Saved trained model files
│   │   └── model.pkl          # Pickled scikit-learn model
│   ├── app.py                 # Main Flask server entrypoint (defines routes, loads model)
│   └── requirements.txt       # Python dependencies (Flask, scikit-learn, etc.)
│
├── frontend/                  # Static website files
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   └── script.js          # API client code
│   └── index.html             # Application homepage
│
├── .gitattributes             # Git configuration for path attributes
├── .gitignore                 # Version control file exclusions
├── LICENSE                    # Project license configuration
└── README.md                  # Project documentation (this file)
```

---

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Flask, NumPy, scikit-learn, Flask-CORS
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

## 🚀 Running the Project

### 1. Backend Setup (Flask API)

Navigate to the `backend/` directory:

```bash
cd backend
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run the backend development server:

```bash
python app.py
```

The backend API will run at `http://127.0.0.1:5000/`.

---

### 2. Frontend Setup

The frontend runs entirely on standard static files. You can:
- Open `frontend/index.html` directly in any browser.
- Serve it using a local static server like `Live Server` in VS Code or Python's built-in HTTP server:
  ```bash
  cd frontend
  python -m http.server 8000
  ```
  Then navigate to `http://localhost:8000/` in your browser.

---

## 🧬 Machine Learning Model Features

The backend requires the following four numerical features in JSON format to generate a prediction:
1. `study_hours` (float): Number of daily study hours.
2. `attendance` (float): Attendance percentage (e.g., 85).
3. `previous_score` (float): Score/marks in previous assessments.
4. `sleep_hours` (float): Daily average sleep hours.
