from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Fix CORS issues

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None

@app.route('/')
def home():
    return "Student Marks Predictor API Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        study = float(data['study_hours'])
        attendance = float(data['attendance'])
        previous = float(data['previous_score'])
        sleep = float(data['sleep_hours'])

        # ✅ 4 FEATURES (IMPORTANT)
        features = np.array([[study, attendance, previous, sleep]])

        prediction = model.predict(features)[0]

        return jsonify({
            "predicted_marks": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)