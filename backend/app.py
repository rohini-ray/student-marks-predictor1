from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Fix CORS issues

# Load model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except:
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