# Script to preprocess data.
import pandas as pd


def preprocess_data(file_path, output_path):
    data = pd.read_csv(file_path)
    data["text"] = data["text"].str.lower()
    data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")
