from fastapi import APIRouter, File, UploadFile
from app.services.ocr_service import extract_text_from_image
from app.services.openai_service import generate_flashcards  # Import the OpenAI function
from app.models.response_schemas import FlashcardResponse
import asyncio

router = APIRouter()

@router.post("/generate_flashcards", summary="Extract Arabic text from an image and generate flashcards", response_model=FlashcardResponse)
async def generate_flashcards_from_image(file: UploadFile = File(...)):
    try:
        # Step 1: Extract text from the uploaded image
        words = await extract_text_from_image(file)

        # Step 2: Generate flashcards using OpenAI
        flashcards = await generate_flashcards(words)

        # Return both extracted words and generated flashcards
        return {
            "extracted_words": words,
            "flashcards": flashcards
        }
    except Exception as e:
        return {"error": str(e)}
