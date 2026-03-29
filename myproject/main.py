import streamlit as st
import pandas as pd
import pickle

# Load model
with open("cox_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("PDAC Risk Prediction Tool")

st.write("Enter patient details:")

# --- Inputs ---
age = st.number_input("Age", 30, 100, 60)
stage = st.selectbox("Stage", [1, 2, 3, 4])
grade = st.selectbox("Grade", [1, 2, 3])

glycan1 = st.number_input("Glycan Biomarker 1", 0.0, 10.0, 1.0)
glycan2 = st.number_input("Glycan Biomarker 2", 0.0, 10.0, 1.0)

# --- Prediction ---
if st.button("Predict Risk"):

    input_df = pd.DataFrame({
        'age': [age],
        'stage': [stage],
        'grade': [grade],
        'glycan1': [glycan1],
        'glycan2': [glycan2]
    })

    risk_score = model.predict_partial_hazard(input_df)[0]

    # Convert to category (you can tune thresholds)
    if risk_score < 0.8:
        risk = "Low Risk"
    elif risk_score < 1.5:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader(f"Risk Score: {risk_score:.2f}")
    st.success(f"Predicted Group: {risk}")