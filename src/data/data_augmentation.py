import logging
import random

import backoff
import nltk
import requests
import spacy
from nltk.corpus import wordnet

# Load Spacy model for NER and tokenization
nlp = spacy.load("en_core_web_sm")

class DataAugmentation:
    def __init__(self, text):
        self.text = text
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=5)
    def augment_with_external_api(self, api_url="https://api.text-augment.com/paraphrase"):
        """Augment text by calling an external paraphrasing API with backoff for robustness."""
        try:
            response = requests.post(api_url, json={"text": self.text})
            if response.status_code == 200:
                return response.json().get('paraphrased_text', self.text)
            return self.text
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {e}")
            return self.text

    def back_translate(self, target_lang='fr'):
        """Perform back-translation using an external translation service (mocked)."""
        translated_text = self.translate_to_language(target_lang)
        return self.translate_to_language('en', translated_text)

    def translate_to_language(self, lang, text=None):
        """Translate text using a translation API."""
        try:
            # Mocking API call, replace with real implementation
            return text or self.text
        except Exception as e:
            self.logger.error(f"Translation failed: {e}")
            return self.text

    def augment_with_synonyms(self):
        """Replace words with synonyms to create variations."""
        nltk.download('wordnet')
        words = self.text.split()
        augmented_texts = []
        for word in words:
            synonyms = wordnet.synsets(word)
            if synonyms:
                lemma = synonyms[0].lemmas()[0].name()
                if lemma != word:
                    new_text = self.text.replace(word, lemma)
                    augmented_texts.append(new_text)
        return augmented_texts

    def named_entity_replacement(self):
        """Replace named entities with generic tags for more generalization."""
        doc = nlp(self.text)
        augmented_text = self.text
        for ent in doc.ents:
            augmented_text = augmented_text.replace(ent.text, f"<{ent.label_}>")
        return augmented_text

    def shuffle_sentences(self):
        """Randomly shuffle sentences within the text for variety."""
        sentences = list(nlp(self.text).sents)
        random.shuffle(sentences)
        return " ".join([sent.text for sent in sentences])

    def augment(self):
        """Combine various augmentation techniques."""
        augmented = [
            self.augment_with_external_api(),
            self.back_translate(),
            *self.augment_with_synonyms(),
            self.named_entity_replacement(),
            self.shuffle_sentences()
        ]
        return list(set(augmented))  # Return unique augmentations

if __name__ == "__main__":
    text = "John visited New York City last weekend to attend a conference."
    augmenter = DataAugmentation(text)
    augmented_texts = augmenter.augment()
    for aug in augmented_texts:
        print(aug)
