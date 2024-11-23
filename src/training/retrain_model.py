# File: retrain_model.py
# Automated model retraining based on user feedback

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load feedback data
try:
    feedback_data = pd.read_csv("feedback.csv")
except FileNotFoundError:
    print("No feedback data available for retraining.")
    exit()

# Prepare training data
X = feedback_data["model-response"]
y = feedback_data["rating"]

# Feature extraction - Example using simple vectorization
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

# Split data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X_vect, y, test_size=0.2, random_state=42
)

# Retrain the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
val_accuracy = model.score(X_val, y_val)
print(f"Validation Accuracy after Retraining: {val_accuracy:.2f}")

# Save the retrained model
joblib.dump(model, "model/retrained_model.pkl")
print("Model retrained and saved successfully.")
