# Script to validate data.
def validate_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    assert 'text' in data.columns, "Missing 'text' column."
    print(f"Data validation passed for {file_path}")
