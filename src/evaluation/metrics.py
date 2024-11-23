from sklearn.metrics import accuracy_score, f1_score


def evaluate_predictions(predictions, labels):
    """
    Evaluate predictions using accuracy and F1 score.
    """
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions, average="weighted")
    return {"accuracy": accuracy, "f1_score": f1}
