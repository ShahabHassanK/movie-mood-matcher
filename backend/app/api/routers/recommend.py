# backend/app/api/routers/recommend.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from backend.app.core.recommender import get_recommendations

router = APIRouter()

class RecommendationRequest(BaseModel):
    traits: List[str]
    top_n: int = 5

class MovieRecommendation(BaseModel):
    title: str
    year: int
    overview: str

class RecommendationResponse(BaseModel):
    recommendations: List[MovieRecommendation]

@router.post("/api/recommend", response_model=RecommendationResponse)
async def recommend_movies(request: RecommendationRequest):
    """
    Get movie recommendations based on user traits
    
    Parameters:
    - traits: List of trait strings from quiz answers (e.g., ["genre_comedy", "mood_happy"])
    - top_n: Number of recommendations to return (default: 5)
    
    Returns:
    - List of recommended movies with title, year, and genres
    """
    try:
        recommendations = get_recommendations(request.traits, request.top_n)
        
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="No recommendations found for the given traits"
            )
            
        return {"recommendations": recommendations}
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating recommendations: {str(e)}"
        )