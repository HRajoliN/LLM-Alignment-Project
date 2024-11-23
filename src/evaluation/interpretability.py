def explain_model_predictions(model, tokenizer, text):
    """
    Explain model predictions using attention scores.
    """
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs, output_attentions=True)
    attentions = outputs.attentions
    return attentions
