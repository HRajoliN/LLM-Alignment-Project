import random
import pandas as pd
import os
from tqdm import tqdm

def generate_synthetic_data(output_path, num_samples=1000):
    """
    Generate a synthetic dataset for LLM training and save it as a CSV file.

    Args:
        output_path (str): Path to save the generated dataset.
        num_samples (int): Number of samples to generate.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Define synthetic prompts and responses
    prompts = [
        "Explain the importance of AI in modern technology.",
        "What is the role of ethics in AI?",
        "Describe the applications of machine learning in healthcare.",
        "How does reinforcement learning work?",
        "Write a creative story about a robot exploring space.",
        "Summarize the concept of blockchain technology.",
        "Explain how neural networks are trained.",
        "What are the key differences between supervised and unsupervised learning?",
    ]

    responses = [
        "AI plays a critical role in improving efficiency and automating tasks.",
        "Ethics in AI ensures that technology serves humanity responsibly.",
        "Machine learning is revolutionizing diagnostics and personalized treatments.",
        "Reinforcement learning involves training agents through trial and error.",
        "Once upon a time, a robot named Astro ventured into the vast unknown.",
        "Blockchain ensures secure and decentralized transaction recording.",
        "Neural networks are trained using backpropagation and gradient descent.",
        "Supervised learning uses labeled data, while unsupervised learning finds patterns.",
    ]

    # Generate synthetic data with a progress bar
    data = []
    for _ in tqdm(range(num_samples), desc="Generating synthetic data"):
        prompt = random.choice(prompts)
        response = random.choice(responses)
        data.append({"text": f"Q: {prompt} A: {response}"})

    # Save data as a CSV
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"\nSynthetic data with {num_samples} samples saved to {output_path}")

if __name__ == "__main__":
    import argparse

    # Command-line interface for flexibility
    parser = argparse.ArgumentParser(description="Generate synthetic data for LLM training.")
    parser.add_argument(
        "--output", type=str, required=True, help="Path to save the generated synthetic data."
    )
    parser.add_argument(
        "--num-samples", type=int, default=1000, help="Number of synthetic samples to generate."
    )

    args = parser.parse_args()
    generate_synthetic_data(output_path=args.output, num_samples=args.num_samples)
