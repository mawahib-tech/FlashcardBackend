from pydantic import BaseModel
from typing import List, Optional

class FlashcardResponse(BaseModel):
    type: str  # "verb", "noun", or "n/a"
    singular_forms: Optional[List[str]] = []  # List of singular forms for nouns
    plural_forms: Optional[List[str]] = []  # List of plural forms for nouns
    past: Optional[str] = ""  # Past tense for verbs
    present: Optional[str] = ""  # Present tense for verbs
    masdar: Optional[str] = ""  # Masdar for verbs
    bab: Optional[str] = ""  # Bab name (for verbs)
    irregularity: Optional[str] = ""  # Irregularity type (for verbs)
    meaning_english: Optional[str] = ""  # English meaning for both nouns and verbs
