from pydantic import BaseModel
from typing import List, Optional

class ExtractTextResponse(BaseModel):
    extracted_words: List[str]
