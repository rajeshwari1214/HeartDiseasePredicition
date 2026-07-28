import os
import pickle
import numpy as np

from backend.utils import get_result

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "extracted model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Load scaler
with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)


def predict(data):
    """
    Predict heart disease.

    Parameters:
        data (list): List of 13 input features.

    Returns:
        str: Prediction result.
    """

    data = np.array(data).reshape(1, -1)

    # Scale the input
    data = scaler.transform(data)

    # Make prediction
    prediction = model.predict(data)

    # If using a Keras model, convert probability to class
    if hasattr(prediction[0], "__len__"):
        prediction = int(prediction[0][0] >= 0.5)
    else:
        prediction = int(prediction[0])

    return get_result(prediction)