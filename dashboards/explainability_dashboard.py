# SHAP-based Explainability Dashboard using Streamlit

import streamlit as st
import shap
import matplotlib.pyplot as plt
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/retrained_model.pkl')

# Sample data for explanation
X_sample = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Feature3': [2, 3, 4, 5, 6]
})

# Title of the dashboard
st.title("🧐 Model Explainability Dashboard")

# Explain predictions using SHAP
explainer = shap.Explainer(model, X_sample)
shap_values = explainer(X_sample)

# Plot SHAP Summary Plot
st.header("SHAP Summary Plot")
fig_summary = shap.summary_plot(shap_values, X_sample, show=False)
st.pyplot(fig_summary)

# Feature Importance
st.header("Feature Importance")
shap.plots.bar(shap_values)
