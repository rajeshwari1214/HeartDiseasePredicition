# ❤️ Heart Disease Prediction System

A Machine Learning-based **Heart Disease Prediction System** built using **Python**, **Streamlit**, and **Scikit-learn/TensorFlow**. This application predicts whether a patient is likely to have heart disease based on various medical parameters entered by the user.

---

## 📌 Features

- User-friendly Streamlit web interface
- Predicts heart disease using a trained Machine Learning model
- Input validation for patient details
- Modular project structure (Frontend & Backend)
- Pre-trained model stored as `.pkl`
- Easy to run locally

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- Pickle

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── backend/
│   ├── predict.py
│   └── utils.py
│
├── frontend/
│   └── streamlit_app.py
│
├── model/
│   ├── extracted model.pkl
│   └── scaler.pkl
│
├── static/
├── templates/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

The model uses the following medical parameters for prediction:

| Feature | Description |
|----------|-------------|
| Age | Age of the patient |
| Sex | Male/Female |
| Chest Pain Type | Type of chest pain |
| Resting Blood Pressure | Blood pressure (mm Hg) |
| Cholesterol | Serum cholesterol (mg/dl) |
| Fasting Blood Sugar | Above 120 mg/dl |
| Resting ECG | Electrocardiographic results |
| Maximum Heart Rate | Maximum heart rate achieved |
| Exercise Induced Angina | Yes/No |
| Oldpeak | ST depression induced by exercise |
| Slope | Slope of peak exercise ST segment |
| Major Vessels | Number of major vessels |
| Thalassemia | Blood disorder type |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction.git
```

Navigate to the project folder:

```bash
cd Heart-Disease-Prediction
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run frontend/streamlit_app.py
```

After running the command, open your browser and visit:

```
http://localhost:8501
```

---

## 🧠 Model Information

The project uses a trained Machine Learning model to classify whether a patient is likely to have heart disease.

The trained model is stored in:

```
model/extracted model.pkl
```

The feature scaler is stored in:

```
model/scaler.pkl
```

---

## 📈 Workflow

1. Load the trained model and scaler.
2. Accept patient information from the Streamlit interface.
3. Preprocess the input data.
4. Scale the input features.
5. Predict heart disease using the trained model.
6. Display the prediction result.

---

## 📷 Application Preview

You can add screenshots of the application here after running it.

Example:

```
screenshots/home.png
screenshots/result.png
```

---

## 📚 Future Improvements

- Model performance visualization
- Risk probability score
- User authentication
- Patient history storage
- Cloud deployment
- Medical report generation
- Support for multiple machine learning models

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Author

**Taneeru Rajeshwari**

- GitHub: https://github.com/RajeshwariNarayana
- LinkedIn: https://www.linkedin.com/in/t-rajeshwari/

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
