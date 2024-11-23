from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

def fine_tune(model_name, dataset, output_dir):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    args = TrainingArguments(output_dir=output_dir, num_train_epochs=3)
    trainer = Trainer(model=model, args=args, train_dataset=dataset)
    trainer.train()
    model.save_pretrained(output_dir)
