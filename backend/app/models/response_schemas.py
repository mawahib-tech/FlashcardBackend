from pydantic import BaseModel
from typing import List, Dict

class FlashcardResponse(BaseModel):
    extracted_words: List[str]
    flashcards: Dict[str, str]
