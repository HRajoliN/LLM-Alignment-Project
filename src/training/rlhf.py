from transformers import PPOTrainer, PPOConfig

def train_with_rlhf(model, tokenizer, dataset, reward_model):
    config = PPOConfig()
    trainer = PPOTrainer(config=config, model=model, tokenizer=tokenizer, dataset=dataset, reward_model=reward_model)
    trainer.train()
