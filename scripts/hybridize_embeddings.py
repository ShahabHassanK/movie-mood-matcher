import pandas as pd

# Load both datasets
tag_df = pd.read_pickle("data/processed/movies_with_tag_vectors.pkl")
overview_df = pd.read_csv("data/processed/movies_with_overview_embeddings.csv")

# Merge on movieId
merged_df = pd.merge(tag_df, overview_df, on=["movieId", "title"], how="inner")

# Save final hybrid vector
merged_df.to_pickle("data/processed/movies_with_hybrid_embeddings.pkl")
print("✅ Hybrid embeddings saved to data/processed/movies_with_hybrid_embeddings.pkl")

# Optional: check shape
print(f"🧩 Final vector shape per movie: {merged_df.shape}")
