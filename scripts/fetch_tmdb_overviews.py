import pandas as pd
import requests
import time
import os
from dotenv import load_dotenv
from tqdm import tqdm

# Load TMDb API key from tmd.env file
load_dotenv(dotenv_path="tmd.env")
API_KEY = os.getenv("TMDB_API_KEY")

# Base URL to fetch movie details
TMDB_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"

# Load your dataframe with tmdbId (should be present)
df_path = "data/processed/movies_with_tmdb_id.csv"
df = pd.read_csv(df_path)

# Add empty overview column
df['overview'] = None

# Loop through each movie and fetch its overview
for idx, row in tqdm(df.iterrows(), total=len(df)):
    tmdb_id = row['tmdbId']
    
    if pd.isna(tmdb_id):
        continue

    try:
        response = requests.get(TMDB_URL.format(int(tmdb_id), API_KEY))
        if response.status_code == 200:
            movie_data = response.json()
            df.at[idx, 'overview'] = movie_data.get("overview", "")
        else:
            print(f"❌ Failed for tmdbId={tmdb_id}, Status code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error for tmdbId={tmdb_id}: {e}")
    
    time.sleep(0.25)  # TMDb API allows 40 requests per 10 sec

# Save the updated file
output_path = "data/processed/movies_with_overviews.csv"
df.to_csv(output_path, index=False)
print(f"✅ Saved with overviews to {output_path}")