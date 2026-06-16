# 🎓 Students Marks Predictor

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview

**Students Marks Predictor** is a Machine Learning based application that predicts students' marks based on various academic and performance-related factors.

The project uses data preprocessing, exploratory data analysis, and regression algorithms to analyze student data and predict expected marks accurately.

This project demonstrates the complete Machine Learning workflow from data collection to model deployment.

---

## 🎯 Objectives

* Predict student marks using Machine Learning algorithms
* Analyze factors affecting student performance
* Build a data-driven academic prediction system
* Provide accurate predictions using trained ML models

---

## 🚀 Features

✅ Data Cleaning and Preprocessing
✅ Exploratory Data Analysis (EDA)
✅ Feature Engineering
✅ Machine Learning Model Training
✅ Model Evaluation
✅ Marks Prediction System
✅ User-Friendly Interface

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning Libraries

* NumPy
* Pandas
* Scikit-learn

### Data Visualization

* Matplotlib
* Seaborn

### Development Tools

* Jupyter Notebook
* VS Code
* Git & GitHub

### Deployment

* Flask (Web Application)

---

# 📂 Project Structure

```
Students-Marks-Predictor/
│
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
│
├── backend/
│ │
│ ├── app.py
│ ├── model.pkl
│ └── requirements.txt
│
└── frontend/
│
├── index.html
├── script.js
└── style.css
```


## 📁 Directory Description

### 🔹 backend/

Contains the Machine Learning model and backend API implementation.

| File | Description |
|------|-------------|
| `app.py` | Flask backend application that loads the trained ML model and predicts student marks based on user input |
| `model.pkl` | Saved Machine Learning regression model used for marks prediction |
| `requirements.txt` | Python dependencies required to run the backend application |

---

### 🔹 frontend/

Contains the user interface for entering student details and displaying predicted marks.

| File | Description |
|------|-------------|
| `index.html` | Webpage structure containing input fields and prediction interface |
| `style.css` | Frontend styling and responsive UI design |
| `script.js` | Handles user interactions and connects frontend with backend API |

---

### 🔹 Root Files

| File | Description |
|------|-------------|
| `.gitignore` | Specifies files ignored by Git |
| `.gitattributes` | Git repository configuration settings |
| `LICENSE` | Project license information |
| `README.md` | Project documentation |


---

# 🧠 Machine Learning Workflow

## 1. Data Collection

The dataset contains student academic information such as:

* Study Hours
* Previous Scores
* Attendance
* Practice Tests
* Other performance factors

---

## 2. Data Preprocessing

Performed operations:

* Handling missing values
* Removing duplicate data
* Data transformation
* Feature selection
* Train-test splitting

---

## 3. Exploratory Data Analysis

Data visualization techniques:

* Correlation Heatmap
* Distribution Analysis
* Feature Relationship Analysis

---

## 4. Model Training

Machine Learning algorithms used:

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

The best performing model is selected for prediction.

---

# 📊 Model Evaluation

The model performance is evaluated using:

### Mean Absolute Error (MAE)

Measures average prediction error.

### Mean Squared Error (MSE)

Measures squared difference between actual and predicted values.

### R² Score

Shows how accurately the model explains student performance.

Example:

```
Model Accuracy:
R² Score: 0.90+
```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/Students-Marks-Predictor.git
```

## Navigate to Project Directory

```bash
cd Students-Marks-Predictor
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Start Flask server:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

---

# 🔮 Sample Prediction

### Input

```
Study Hours: 7
Previous Score: 85
Attendance: 90
Practice Tests: 8
```

### Output

```
Predicted Marks: 92
```

---

# 📈 Future Enhancements

* Deep Learning based prediction
* AI-based personalized study recommendations
* Student performance dashboard
* Mobile application integration
* Cloud deployment
* Real-time analytics

---

# 👨‍💻 Author

**Your Name**

GitHub:

```
https://github.com/yourusername
```

LinkedIn:

```
https://linkedin.com/in/yourusername
```

---

# 🤝 Contribution

Contributions are welcome!

1. Fork this repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📜 License

This project is licensed under the MIT License.
