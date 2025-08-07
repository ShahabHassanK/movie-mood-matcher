import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import os

# Load data
df_path = "data/processed/movies_with_overviews.csv"
df = pd.read_csv(df_path)

# Drop missing overviews
df = df.dropna(subset=['overview'])

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Compute embeddings
print("🔄 Generating embeddings for overviews...")
embeddings = model.encode(df['overview'].tolist(), show_progress_bar=True)

# Convert to DataFrame
embeddings_df = pd.DataFrame(embeddings)
embeddings_df.columns = [f"overview_emb_{i}" for i in range(embeddings_df.shape[1])]

# Merge with original data
df.reset_index(drop=True, inplace=True)
result_df = pd.concat([df[['movieId', 'title']], embeddings_df], axis=1)

# Save embeddings
output_path = "data/processed/movies_with_overview_embeddings.csv"
result_df.to_csv(output_path, index=False)
print(f"✅ Overview embeddings saved to {output_path}")
