# backend/app/api/routers/questions.py

from fastapi import APIRouter
from backend.app.core.quiz_engine import QuizEngine

router = APIRouter()

@router.get("/api/questions")
def get_questions():
    engine = QuizEngine(num_questions=15)
    selected_questions = engine.get_random_questions()
    
    formatted_questions = []
    for q in selected_questions:
        # Convert options to include both text and traits
        options = [
            {
                "text": option_text,
                "traits": traits 
            } 
            for option_text, traits in q["options"].items()
        ]
        
        formatted_questions.append({
            "question": q["question"],
            "options": options
        })
    
    return formatted_questions