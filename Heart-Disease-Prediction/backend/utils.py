"""
Utility functions for Heart Disease Prediction
"""

def get_result(prediction):
    """
    Convert model prediction into a readable result.
    """

    if prediction == 1:
        return "Heart Disease Detected"

    return "No Heart Disease Detected"