# scripts/simulate_training_pairs.py

import numpy as np
import pandas as pd
import joblib
import random
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.app.core.feature_space import FEATURE_SPACE
from backend.app.core.quiz_engine import run_quiz, vectorize_user_answers, get_random_quiz_questions


# Load your movie embeddings (1512D)
movies_df = pd.read_pickle("data/processed/movies_with_hybrid_embeddings.pkl")
vector_columns = [col for col in movies_df.columns if isinstance(col, int) or str(col).startswith("overview_emb_")]
movie_embeddings = movies_df[vector_columns].to_numpy()

# Simulation config
NUM_SAMPLES = 1000
SAVE_PATH = "data/processed/quiz_to_embedding_dataset.pkl"

def simulate_quiz_response():
    """
    Simulates a quiz by randomly selecting answers for 10 questions.
    Returns a 63D user feature vector.
    """
    quiz = get_random_quiz_questions(n=10)
    traits = []

    for q in quiz:
        option_keys = list(q["options"].keys())
        chosen = random.choice(option_keys)
        traits.extend(q["options"][chosen])

    return vectorize_user_answers(traits)

def generate_dataset(n_samples=NUM_SAMPLES):
    X_user_vectors = []
    Y_movie_vectors = []

    for _ in range(n_samples):
        user_vector = simulate_quiz_response()

        # Simple strategy: randomly choose a movie embedding
        movie_vector = movie_embeddings[random.randint(0, len(movie_embeddings) - 1)]

        X_user_vectors.append(user_vector)
        Y_movie_vectors.append(movie_vector)

    return np.array(X_user_vectors), np.array(Y_movie_vectors)

def save_dataset(X, Y, path=SAVE_PATH):
    with open(path, "wb") as f:
        joblib.dump({"X": X, "Y": Y}, f)
    print(f"✅ Saved simulated dataset: {path} | Shape: X={X.shape}, Y={Y.shape}")

if __name__ == "__main__":
    X, Y = generate_dataset()
    save_dataset(X, Y)
