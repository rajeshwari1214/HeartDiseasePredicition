import streamlit as st
import sys
import os
from pathlib import Path

# Add the project root to path using this file's location so the app works
# no matter which directory Streamlit is launched from.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.predict import predict

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction System")
st.markdown("Enter the patient's clinical details below and click **Predict**.")

st.divider()

# -----------------------------------------------------
# Input Form
# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 45)

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina",
            "Atypical Angina",
            "Non-anginal Pain",
            "Asymptomatic"
        ]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        80,
        250,
        120
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        100,
        700,
        200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        ["No", "Yes"]
    )

with col2:

    restecg = st.selectbox(
        "Resting ECG",
        [
            "Normal",
            "ST-T Wave Abnormality",
            "Left Ventricular Hypertrophy"
        ]
    )

    thalach = st.number_input(
        "Maximum Heart Rate",
        50,
        250,
        150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        0.0,
        10.0,
        1.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope",
        [
            "Upsloping",
            "Flat",
            "Downsloping"
        ]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0,1,2,3,4]
    )

    thal = st.selectbox(
        "Thalassemia",
        [
            "Normal",
            "Fixed Defect",
            "Reversible Defect",
            "Unknown"
        ]
    )

# -----------------------------------------------------
# Convert Inputs
# -----------------------------------------------------

sex = 1 if sex == "Male" else 0

cp = {
    "Typical Angina":0,
    "Atypical Angina":1,
    "Non-anginal Pain":2,
    "Asymptomatic":3
}[cp]

fbs = 1 if fbs == "Yes" else 0

restecg = {
    "Normal":0,
    "ST-T Wave Abnormality":1,
    "Left Ventricular Hypertrophy":2
}[restecg]

exang = 1 if exang == "Yes" else 0

slope = {
    "Upsloping":0,
    "Flat":1,
    "Downsloping":2
}[slope]

thal = {
    "Normal":0,
    "Fixed Defect":1,
    "Reversible Defect":2,
    "Unknown":3
}[thal]

# -----------------------------------------------------
# Predict Button
# -----------------------------------------------------

if st.button("Predict Heart Disease", use_container_width=True):

    input_data = [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]

    result = predict(input_data)

    st.divider()

    if result == "Heart Disease Detected":
        st.error(result)
    else:
        st.success(result)