import re
import pandas as pd

class DataCleaning:
    def __init__(self, df):
        self.df = df

    @staticmethod
    def clean_text(text):
        # Basic cleaning such as removing unwanted characters and converting to lowercase
        return re.sub(r'\W+', ' ', text.lower()).strip()

    def remove_duplicates(self):
        # Remove duplicate rows
        self.df = self.df.drop_duplicates()

    def remove_biases(self):
        # Example of removing biased content, can be expanded
        biased_phrases = ["offensive term 1", "offensive term 2"]
        self.df = self.df[~self.df['text'].str.contains('|'.join(biased_phrases), case=False)]

    def clean_all_text(self):
        # Apply the clean_text method to every row in the 'text' column
        self.df['text'] = self.df['text'].apply(DataCleaning.clean_text)

    def get_cleaned_data(self):
        self.remove_duplicates()
        self.remove_biases()
        self.clean_all_text()
        return self.df

if __name__ == "__main__":
    df = pd.read_csv("raw_data.csv")
    cleaner = DataCleaning(df)
    cleaned_df = cleaner.get_cleaned_data()
    cleaned_df.to_csv("cleaned_data.csv", index=False)
