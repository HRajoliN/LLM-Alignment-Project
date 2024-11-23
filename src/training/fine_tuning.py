from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

def fine_tune_model(model_name, dataset_path, output_dir):
    """
    Fine-tune a pre-trained language model on a given dataset.
    """
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Load dataset
    dataset = load_dataset("csv", data_files=dataset_path)

    # Tokenize the dataset
    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, padding="max_length")
    
    tokenized_dataset = dataset.map(tokenize, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="steps",
        per_device_train_batch_size=8,
        save_steps=500,
        num_train_epochs=3
    )

    # Define Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["validation"],
    )

    # Train the model
    trainer.train()

    # Save the model
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
