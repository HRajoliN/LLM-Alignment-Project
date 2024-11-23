# File: src/training/fine_tuning.py
# Fine-tuning Script with Option to Use Pre-trained Models

import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import BertForSequenceClassification, BertTokenizer

# Load configuration
use_pretrained = True
model_name = "bert-base-uncased"

# Load Dataset
train_data = pd.read_csv("data/processed/train_data.csv")
val_data = pd.read_csv("data/processed/val_data.csv")

# Tokenizer Setup
tokenizer = BertTokenizer.from_pretrained(model_name)

# Custom Dataset Class
class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        inputs = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            max_length=self.max_length,
            padding="max_length",
            return_token_type_ids=True,
            truncation=True,
            return_attention_mask=True,
            return_tensors="pt",
        )
        return {
            "input_ids": inputs["input_ids"].flatten(),
            "attention_mask": inputs["attention_mask"].flatten(),
            "labels": torch.tensor(label, dtype=torch.long),
        }


# Prepare DataLoader for Training
train_dataset = CustomDataset(
    train_data["text"].values, train_data["label"].values, tokenizer, max_length=128
)
val_dataset = CustomDataset(
    val_data["text"].values, val_data["label"].values, tokenizer, max_length=128
)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16)

# Load Model
if use_pretrained:
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
else:
    model = BertForSequenceClassification(config=config)

# Optimizer Setup
optimizer = AdamW(model.parameters(), lr=2e-5)

# Training Loop
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

for epoch in range(3):
    model.train()
    for batch in train_loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)

        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Validation Loop
    model.eval()
    val_loss_total = 0
    correct_predictions = 0
    total = 0
    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            val_loss_total += outputs.loss.item()
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=-1)
            correct_predictions += (predictions == labels).sum().item()
            total += labels.size(0)

    val_loss_avg = val_loss_total / len(val_loader)
    val_accuracy = correct_predictions / total
    print(
        f"Epoch {epoch + 1} - Validation Loss: {val_loss_avg:.4f} - Accuracy: {val_accuracy:.4f}"
    )

# Save Fine-tuned Model
model.save_pretrained("model/fine_tuned_bert")
tokenizer.save_pretrained("model/fine_tuned_bert")
print("Fine-tuned model saved successfully.")
