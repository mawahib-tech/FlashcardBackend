from fastapi import APIRouter, File, UploadFile
from app.services.ocr_service import extract_text_from_image
from app.models.response_schemas import ExtractTextResponse


router = APIRouter()

@router.post("/extract_text", summary="Extract Arabic text from an uploaded image", response_model=ExtractTextResponse)
async def extract_text(file: UploadFile = File(...)):
    try:
        words = await extract_text_from_image(file)
        return {"extracted_words": words}
    except Exception as e:
        return {"error": str(e)}
