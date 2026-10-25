
from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("best_price_model.joblib")


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not isinstance(data, dict):
            return jsonify({"error": "Please send valid JSON input."}), 400

        # These feature names must match train_model.py.
        features = {
            "device_brand": data["device_brand"],
            "os": data["os"],
            "screen_size": float(data["screen_size"]),
            "four_g": data["four_g"],
            "five_g": data["five_g"],
            "rear_camera_mp": float(data["rear_camera_mp"]),
            "front_camera_mp": float(data["front_camera_mp"]),
            "internal_memory": float(data["internal_memory"]),
            "ram": float(data["ram"]),
            "battery": float(data["battery"]),
            "weight": float(data["weight"]),
            "release_year": int(data["release_year"]),
            "days_used": int(data["days_used"])
        }

        # Reject invalid numeric values
        numeric_values = [
            value for value in features.values()
            if isinstance(value, (int, float, np.number))
        ]

        if not all(np.isfinite(value) for value in numeric_values):
            return jsonify({"error": "Numeric inputs must be finite."}), 400

        if features["days_used"] < 0:
            return jsonify({"error": "Days used cannot be negative."}), 400

        input_df = pd.DataFrame([features])

        prediction = float(model.predict(input_df)[0])

        return jsonify({
            "predicted_used_price_inr": max(0, round(prediction)),
            "currency": "INR",
            "note": (
                "Estimated price based on the training dataset. "
                "The INR training labels are calculated estimates, "
                "not independently verified resale prices."
            )
        })

    except (KeyError, TypeError, ValueError, OverflowError) as e:
        return jsonify({
            "error": f"Invalid or missing input: {e}"
        }), 400

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({
            "error": "Prediction failed. Check the server terminal."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
