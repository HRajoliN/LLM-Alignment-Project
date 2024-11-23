from transformers import PPOConfig, PPOTrainer


def train_with_rlhf(model, tokenizer, reward_model, dataset):
    """
    Train a language model using Reinforcement Learning from Human Feedback (RLHF).
    """
    # PPO Configuration
    ppo_config = PPOConfig()

    # Create PPO Trainer
    trainer = PPOTrainer(
        config=ppo_config,
        model=model,
        tokenizer=tokenizer,
        dataset=dataset,
        reward_model=reward_model,
    )

    # Train the model
    trainer.train()
