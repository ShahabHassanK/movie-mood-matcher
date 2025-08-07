# backend/app/core/config.py
from pathlib import Path

class Settings:
    def __init__(self):
        self.EMBEDDINGS_PATH = Path("data/processed/movies_with_hybrid_embeddings.pkl").resolve()
        self.OVERVIEW_PATH = Path("data/processed/movies_with_overviews.csv").resolve()

        # Verify paths
        if not self.EMBEDDINGS_PATH.exists():
            available = list(self.EMBEDDINGS_PATH.parent.glob("*"))
            raise FileNotFoundError(
                f"Embeddings not found at {self.EMBEDDINGS_PATH}\n"
                f"Available files: {available}"
            )

settings = Settings()