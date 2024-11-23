from transformers import AutoTokenizer


def tokenize_texts(texts, model_name="bert-base-uncased", max_length=128):
    """
    Tokenize a list of texts using a pre-trained tokenizer.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer(
        texts, max_length=max_length, truncation=True, padding=True, return_tensors="pt"
    )
