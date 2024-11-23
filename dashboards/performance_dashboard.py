# Expanded Performance Dashboard using Streamlit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

# Title of the dashboard
st.title("📊 LLM Alignment Assistant Expanded Performance Dashboard")

# Sidebar filters for the dashboard
st.sidebar.header("Filters")
epochs = st.sidebar.slider("Select Epoch Range", 1, 50, (1, 10))

# Mock Data - Training & Validation Loss
st.header("Training and Validation Loss")
train_loss = np.linspace(0.8, 0.1, 50)
val_loss = np.linspace(0.9, 0.15, 50)

filtered_epochs = range(epochs[0], epochs[1] + 1)
filtered_train_loss = train_loss[epochs[0] - 1 : epochs[1]]
filtered_val_loss = val_loss[epochs[0] - 1 : epochs[1]]

fig, ax = plt.subplots()
ax.plot(filtered_epochs, filtered_train_loss, label="Training Loss", color="blue")
ax.plot(filtered_epochs, filtered_val_loss, label="Validation Loss", color="red")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")
ax.set_title("Training vs Validation Loss")
ax.legend()

# Display the plot
st.pyplot(fig)

# Performance Metrics
st.header("Model Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Training Loss", f"{train_loss[-1]:.4f}")
col2.metric("Validation Loss", f"{val_loss[-1]:.4f}")
col3.metric("Accuracy", "92.5%")

# Confusion Matrix
st.header("Confusion Matrix")
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
cm = confusion_matrix(y_true, y_pred)
fig_cm, ax_cm = plt.subplots()
ConfusionMatrixDisplay(cm).plot(ax=ax_cm)
st.pyplot(fig_cm)

# Bias Metrics Visualization
st.header("Bias Metrics by Group")
try:
    bias_metrics_df = pd.read_csv("bias_metrics.csv")
    st.dataframe(bias_metrics_df)
except FileNotFoundError:
    st.warning(
        "Bias metrics data not found. Please generate bias metrics using `bias_analysis.py`."
    )

# Instructions for running the dashboard
st.markdown("---")
st.markdown("**Instructions:** To run this dashboard, use the command:")
st.code("streamlit run performance_dashboard.py", language="bash")
