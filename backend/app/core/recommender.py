# backend/app/core/recommender.py
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from backend.app.core.config import settings
import warnings
import logging
from typing import List, Dict
import os
import random

# Configure environment
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
warnings.filterwarnings("ignore")

# Global cache with lazy loading
_EMBEDDINGS_CACHE = {
    'movies_df': None,
    'movie_embeddings': None,
    'overviews_df': None,
    'model': None
}

def load_resources():
    """Optimized resource loader with proper caching"""
    if _EMBEDDINGS_CACHE['movies_df'] is None:
        _EMBEDDINGS_CACHE['movies_df'] = pd.read_pickle(settings.EMBEDDINGS_PATH)
        
    if _EMBEDDINGS_CACHE['movie_embeddings'] is None:
        df = _EMBEDDINGS_CACHE['movies_df']
        _EMBEDDINGS_CACHE['movie_embeddings'] = {
            'hybrid': np.array(df.iloc[:, -1512:].values),
            'overview': np.array(df.iloc[:, -384:].values)  # Last 384 cols are overview
        }
    
    if _EMBEDDINGS_CACHE['overviews_df'] is None:
        _EMBEDDINGS_CACHE['overviews_df'] = pd.read_csv(
            settings.OVERVIEW_PATH,
            usecols=['title', 'year', 'overview'],
            dtype={'year': 'Int64'}
        )
    
    if _EMBEDDINGS_CACHE['model'] is None:
        _EMBEDDINGS_CACHE['model'] = SentenceTransformer(
            'all-MiniLM-L6-v2',
            device='cpu',
            use_auth_token=False
        )
    
    return _EMBEDDINGS_CACHE

def generate_prompt(traits: List[str]) -> str:
    """
    Generates a natural language prompt for movie recommendations based on user traits.
    Handles all combinations of genres, moods, tones, settings, and themes.
    """
    
    # Category mappings with natural language equivalents
    category_map = {
        'genre': {
            'action': "action-packed",
            'comedy': "hilarious",
            'romance': "romantic",
            'horror': "terrifying",
            'sci_fi': "sci-fi",
            'drama': "dramatic",
            'fantasy': "fantasy",
            'thriller': "thrilling",
            'animation': "animated"
        },
        'mood': {
            'happy': "feel-good",
            'sad': "emotional",
            'romantic': "heartwarming",
            'spooky': "chilling",
            'nostalgic': "nostalgic",
            'excited': "adrenaline-filled"
        },
        'tone': {
            'dark': "dark and gritty",
            'lighthearted': "light-hearted",
            'uplifting': "inspiring",
            'realistic': "gritty and realistic",
            'absurdist': "quirky and absurd"
        },
        'setting': {
            'future': "futuristic",
            'historical': "historical",
            'space': "set in space",
            'smalltown': "small-town",
            'fantasyworld': "fantasy world"
        },
        'theme': {
            'love': "love story",
            'friendship': "tale of friendship",
            'redemption': "story of redemption",
            'war': "war-time story",
            'coming_of_age': "coming-of-age story"
        },
        'pacing': {
            'fast': "fast-paced",
            'slow': "slow-burning",
            'medium': "moderately paced"
        }
    }

    # Build prompt components
    components = {
        'genres': [],
        'moods': [],
        'tones': [],
        'settings': [],
        'themes': [],
        'pacing': []
    }

    # Categorize traits
    for trait in traits:
        prefix, *value_parts = trait.split('_')
        value = '_'.join(value_parts)
        
        if prefix in components:
            category_dict = category_map.get(prefix, {})
            display_value = category_dict.get(value, value.replace('_', ' '))
            components[prefix].append(display_value)

    # Construct natural language prompt
    prompt_parts = []
    
    # Genre handling
    if components['genres']:
        if len(components['genres']) > 1:
            genre_str = ", ".join(components['genres'][:-1]) + " and " + components['genres'][-1]
            prompt_parts.append(f"{genre_str} movie")
        else:
            prompt_parts.append(f"{components['genres'][0]} movie")

    # Mood and tone
    mood_tone = []
    if components['moods']:
        mood_tone.append(f"that feels {' and '.join(components['moods'])}")
    if components['tones']:
        mood_tone.append(f"with a {', '.join(components['tones'])} tone")
    if mood_tone:
        prompt_parts.append(" ".join(mood_tone))

    # Setting
    if components['settings']:
        if len(components['settings']) > 1:
            prompt_parts.append(f"set in either {' or '.join(components['settings'])}")
        else:
            prompt_parts.append(f"set in {components['settings'][0]}")

    # Theme
    if components['themes']:
        prompt_parts.append(f"about {' and '.join(components['themes'])}")

    # Pacing
    if components['pacing']:
        prompt_parts.append(f"with {components['pacing'][0]} pacing")

    # Final prompt assembly
    if not prompt_parts:  # Default case if no traits
        base_prompt = "Recommend a well-rated movie"
    else:
        base_prompt = "Recommend a"
    
    full_prompt = " ".join([base_prompt] + prompt_parts)
    
    # Add quality boosters
    quality_boosters = [
        "with great cinematography",
        "that's critically acclaimed",
        "with memorable characters",
        "that tells a compelling story"
    ]
    
    if len(prompt_parts) > 0:  # Only add boosters if we have specific traits
        full_prompt += ", " + random.choice(quality_boosters)
    
    return full_prompt + "."

def get_recommendations(user_traits: List[str], top_n: int = 5) -> List[Dict]:
    try:
        cache = load_resources()
        movies_df = cache['movies_df']
        overview_embeddings = cache['movie_embeddings']['overview']
        overviews_df = cache['overviews_df']
        model = cache['model']
        
        # Generate optimized prompt
        prompt = generate_prompt(user_traits)
        
        # Get embedding (normalized for better similarity)
        prompt_embedding = model.encode(
            [prompt], 
            convert_to_numpy=True,
            normalize_embeddings=True
        )[0]
        
        # Compute similarities
        similarities = cosine_similarity(
            [prompt_embedding],
            overview_embeddings
        )[0]
        
        # Get top N unique movies
        top_indices = np.argsort(similarities)[-top_n*3:][::-1]  # Get extra for filtering
        seen_titles = set()
        results = []
        
        for idx in top_indices:
            movie = movies_df.iloc[idx]
            title = movie["title"]
            
            # Skip duplicates and verify year exists
            if title in seen_titles or pd.isna(movie["year"]):
                continue
            seen_titles.add(title)
            
            # Get overview
            overview_match = overviews_df[
                (overviews_df['title'] == title) & 
                (overviews_df['year'] == int(movie["year"]))
            ]
            
            if not overview_match.empty:
                overview = overview_match.iloc[0]['overview']
                if pd.isna(overview):
                    overview = ""
            else:
                overview = ""
            
            results.append({
                "title": title,
                "year": int(movie["year"]),
                "overview": overview
            })
            
            if len(results) >= top_n:
                break
                
        return results
    
    except Exception as e:
        logging.error(f"Recommendation error: {str(e)}", exc_info=True)
        return []
