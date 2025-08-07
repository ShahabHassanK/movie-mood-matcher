# backend/app/core/quiz_engine.py
import random
from typing import List
from backend.app.core.questions_pool import QUESTION_POOL

class QuizEngine:
    def __init__(self, num_questions: int = 15):
        self.num_questions = num_questions

    def get_random_questions(self) -> List[dict]:
        return random.sample(QUESTION_POOL, self.num_questions)

    @staticmethod
    def extract_traits_from_answers(answers: dict) -> List[str]:
        traits = []
        for q_idx, option_idx in answers.items():
            question = QUESTION_POOL[q_idx]
            option_key = list(question["options"].keys())[option_idx]
            traits.extend(question["options"][option_key])
        return traits