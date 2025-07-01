import streamlit as st

st.title("🩺 Diabetes Predictor")

glucose = st.slider("Glucose Level", 0, 200, 120)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
age = st.slider("Age", 10, 80, 30)

if st.button("Predict"):
    result = "Diabetic" if glucose > 140 and bmi > 30 else "Non-Diabetic"
    st.success(f"Prediction: {result}")
