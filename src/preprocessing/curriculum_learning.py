import pandas as pd

class CurriculumLearning:
    def __init__(self, df):
        self.df = df

    def calculate_difficulty(self, text):
        # Mock difficulty score: length of text as proxy
        return len(text.split())

    def sort_by_difficulty(self):
        self.df['difficulty'] = self.df['text'].apply(self.calculate_difficulty)
        return self.df.sort_values(by='difficulty')

if __name__ == "__main__":
    df = pd.read_csv("cleaned_data.csv")
    curriculum = CurriculumLearning(df)
    sorted_df = curriculum.sort_by_difficulty()
    sorted_df.to_csv("sorted_data.csv", index=False)
