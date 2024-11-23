from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_reward_model(model_name="bert-base-uncased"):
    """
    Load a pre-trained reward model for RLHF.
    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
