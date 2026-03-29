import streamlit as st
import pandas as pd
import math

st.title("PDAC Risk Prediction Tool")

st.write("Enter patient details:")

# --- Inputs ---
age = st.number_input("Age", 30, 100, 60)
stage = st.selectbox("Stage", [1, 2, 3, 4])
grade = st.selectbox("Grade", [1, 2, 3])

glycan1 = st.number_input("Glycan Biomarker 1", 0.0, 10.0, 1.0)
glycan2 = st.number_input("Glycan Biomarker 2", 0.0, 10.0, 1.0)

# --- Example Cox Model Coefficients ---
beta_age = 0.02
beta_stage = 0.5
beta_grade = 0.3
beta_glycan1 = 0.4
beta_glycan2 = 0.35

# --- Prediction ---
if st.button("Predict Risk"):

    linear_score = (
        beta_age * age +
        beta_stage * stage +
        beta_grade * grade +
        beta_glycan1 * glycan1 +
        beta_glycan2 * glycan2
    )

    risk_score = math.exp(linear_score)

    # Risk category
    if risk_score < 0.8:
        risk = "Low Risk"
    elif risk_score < 1.5:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader(f"Risk Score: {risk_score:.2f}")
    st.success(f"Predicted Group: {risk}")
