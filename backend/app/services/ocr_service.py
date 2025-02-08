import io
from PIL import Image
import pytesseract
from app.utils.image_processing import preprocess_image
from app.utils.image_processing import minimal_preprocess
from app.utils.image_processing import clean_extracted_text
import re

async def extract_text_from_image(file) -> list:
    """Extract and clean text from an uploaded image."""
    # Read the image from the file
    image = Image.open(io.BytesIO(await file.read()))

    # Preprocess the image (resize, thresholding, etc.)
    processed_image = minimal_preprocess(image)

    # Extract text using pytesseract with Arabic language setting
    text = pytesseract.image_to_string(processed_image, lang='ara')

    # Split text into individual words and remove empty entries
    words = [word.strip() for word in text.split() if word.strip()]
    words = clean_extracted_text(words)
    processed_words = [re.sub(r'[^\w\s\u0600-\u06FF]', '', word) for word in words]

    return processed_words
