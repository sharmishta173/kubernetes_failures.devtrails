from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("model.h5")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON request
        data = request.get_json()

        if "data" not in data:
            return jsonify({"error": "Missing 'data' key in request"}), 400

        # Reshape the input data for the model
        input_data = np.array(data["data"]).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(input_data)
        result = float(prediction[0][0])  # Convert NumPy array output to float

        return jsonify({"Prediction": result})  # Return the prediction in JSON format

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message and HTTP 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
