import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer

def ppo_training(config):
    trainer = PPOTrainer(config=config)
    for i in range(50):
        results = trainer.train()
        print(f"Iteration {i}, reward: {results['episode_reward_mean']}")

if __name__ == "__main__":
    ray.init()
    config = {
        "env": "CartPole-v0",
        "num_workers": 2,
        "lr": tune.grid_search([0.0001, 0.001, 0.01]),
        "train_batch_size": tune.grid_search([4000, 8000]),
    }
    tune.run(ppo_training, config=config)
