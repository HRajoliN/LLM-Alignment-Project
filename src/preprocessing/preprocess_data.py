import re

import pandas as pd
from sklearn.model_selection import train_test_split

# Load original and augmented data
try:
    original_data = pd.read_csv("data/raw/synthetic_data.csv")
    augmented_data = pd.read_csv("data/processed/augmented_training_data.csv")
except FileNotFoundError:
    print(
        "Error: One or more of the input files not found. Make sure the paths are correct."
    )
    exit()

# Combine datasets
combined_data = pd.concat([original_data, augmented_data], ignore_index=True)

# Basic text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)  # Remove non-alphanumeric characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text


# Apply text cleaning
combined_data["text"] = combined_data["text"].apply(clean_text)

# Check for missing values and handle them
if combined_data.isnull().values.any():
    print("Warning: Missing values detected. Filling with empty strings.")
    combined_data.fillna("", inplace=True)

# Splitting the combined dataset into training and validation sets
train_data, val_data = train_test_split(combined_data, test_size=0.2, random_state=42)

# Save processed datasets
train_data.to_csv("data/processed/train_data.csv", index=False)
val_data.to_csv("data/processed/val_data.csv", index=False)
print("Combined and processed datasets saved for training and validation.")
