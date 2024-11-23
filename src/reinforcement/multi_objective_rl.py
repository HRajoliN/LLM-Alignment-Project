import numpy as np


class MultiObjectiveRL:
    def __init__(self, reward_weights):
        self.reward_weights = reward_weights

    def compute_combined_reward(self, rewards):
        # Rewards is a dict, for example: {"bias_reward": x, "quality_reward": y}
        return sum(self.reward_weights[key] * rewards[key] for key in rewards)

    def update_policy(self, rewards):
        combined_reward = self.compute_combined_reward(rewards)
        # Update model policy based on combined_reward
        print(f"Updating policy with reward: {combined_reward}")

if __name__ == "__main__":
    rewards = {"bias_reward": 0.8, "quality_reward": 0.9}
    rl_agent = MultiObjectiveRL({"bias_reward": 0.5, "quality_reward": 1.0})
    rl_agent.update_policy(rewards)
