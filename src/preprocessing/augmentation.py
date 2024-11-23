import random
import re
import spacy
import nltk
from nltk.corpus import stopwords
from spellchecker import SpellChecker

# Load Spacy model for tokenization
nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
spell = SpellChecker()

class PreprocessingAugmentation:
    def __init__(self, text):
        self.text = text

    def random_insertion(self):
        """Randomly insert contextually relevant words to make data varied without changing the meaning."""
        insert_words = ["however", "moreover", "similarly", "therefore"]
        words = self.text.split()
        insert_position = random.randint(0, len(words))
        words.insert(insert_position, random.choice(insert_words))
        return " ".join(words)

    def spelling_variations(self):
        """Introduce some common spelling variations to make model robust."""
        words = self.text.split()
        misspelled_words = spell.unknown(words)
        for word in misspelled_words:
            corrected_word = spell.correction(word)
            if corrected_word:
                self.text = self.text.replace(word, corrected_word)
        return self.text

    def remove_stopwords(self):
        """Remove stopwords to prepare data for training."""
        stop_words = set(stopwords.words('english'))
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered_words)

    def lowercase_and_clean(self):
        """Convert text to lowercase and remove special characters."""
        cleaned_text = re.sub(r'\W+', ' ', self.text.lower())
        return cleaned_text

    def contextual_replacement(self):
        """Replace words with contextually similar ones using Spacy similarity."""
        doc = nlp(self.text)
        replaced_text = self.text
        for token in doc:
            if token.has_vector and token.is_alpha and token.prob < -7:
                similar_word = token.similarity(nlp("sample"))
                if similar_word > 0.7:  # Replace with a similar word if similarity is high enough
                    replaced_text = replaced_text.replace(token.text, "example")
        return replaced_text

    def augment(self):
        """Apply a combination of augmentations."""
        self.text = self.lowercase_and_clean()
        self.text = self.spelling_variations()
        self.text = self.random_insertion()
        self.text = self.contextual_replacement()
        return self.text

if __name__ == "__main__":
    text = "The colour of the sky is beautiful and vibrant, similar to the sea."
    augmenter = PreprocessingAugmentation(text)
    augmented_text = augmenter.augment()
    print(augmented_text)
