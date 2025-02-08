from fastapi import APIRouter, File, UploadFile
from app.services.ocr_service import extract_text_from_image
from app.services.openai_service import generate_flashcards  # Import the OpenAI function
from app.models.response_schemas import FlashcardResponse
import asyncio

router = APIRouter()

@router.post("/generate_flashcards", summary="Generate detailed flashcards from Arabic words", response_model=FlashcardResponse)
async def generate_flashcards_from_image(file: UploadFile = File(...)):
    try:
        # Step 1: Extract text from the uploaded image
        words = await extract_text_from_image(file)

        # Step 2: Generate flashcards using OpenAI for each word
        flashcards = {}
        for word in words:
            flashcard = await generate_flashcards(word)
            flashcards[word] = flashcard

        # Return both extracted words and generated flashcards
        return {
            "extracted_words": words,
            "flashcards": flashcards
        }
    except Exception as e:
        return {"error": str(e)}
