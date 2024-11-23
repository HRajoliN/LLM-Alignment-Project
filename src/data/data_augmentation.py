# Data Augmentation Script

from googletrans import Translator
from transformers import pipeline
import pandas as pd
import random

# Load dataset
data = pd.read_csv('data/raw/synthetic_data.csv')

# Translator for back-translation
translator = Translator()

# Summarization for paraphrasing
paraphraser = pipeline("summarization")

def back_translation(text, target_language="fr"):
    # Translate to target language and back to English
    translated_text = translator.translate(text, dest=target_language).text
    back_translated_text = translator.translate(translated_text, dest="en").text
    return back_translated_text

def paraphrase(text):
    # Use summarization as a paraphrasing tool
    paraphrased = paraphraser(text, max_length=100, min_length=30, do_sample=False)
    return paraphrased[0]['summary_text']

augmented_texts = []
original_texts = data['text'].tolist()

# Perform augmentation
for text in original_texts:
    if random.random() < 0.5:
        augmented_texts.append(back_translation(text))
    else:
        augmented_texts.append(paraphrase(text))

# Save augmented data
augmented_data = pd.DataFrame({'text': augmented_texts, 'label': data['label']})
augmented_data.to_csv('data/processed/augmented_training_data.csv', index=False)
print("Augmented data saved.")
