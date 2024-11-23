import re

def clean_text(text):
    """
    Clean the input text by:
    - Removing special characters
    - Stripping leading/trailing spaces
    - Lowercasing the text
    """
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip().lower()

def clean_dataframe(df, text_column="text"):
    """
    Clean all the text data in the specified column of a DataFrame.
    """
    df[text_column] = df[text_column].apply(clean_text)
    return df
