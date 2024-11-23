# File: mlflow_tracking.py
# Using MLflow to track model experiments

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# MLflow Experiment Tracking
with mlflow.start_run():
    # Model Training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Log Parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)

    # Log Metrics
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    mlflow.log_metric("train_accuracy", train_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)

    # Log Model
    mlflow.sklearn.log_model(model, "random_forest_model")

    print(f"Model saved with train accuracy: {train_accuracy:.2f} and test accuracy: {test_accuracy:.2f}")
