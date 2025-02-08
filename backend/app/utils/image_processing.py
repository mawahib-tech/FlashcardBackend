from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2

def preprocess_image(image: Image.Image) -> Image.Image:
    """Preprocess the image to improve OCR accuracy."""
    # Convert to grayscale
    image = image.convert("L")
    
    # Resize the image to improve text recognition for small text
    width, height = image.size
    image = image.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
    
    # Convert to NumPy array for OpenCV processing
    image_np = np.array(image)
    
    # Apply thresholding to enhance text visibility
    _, thresh_image = cv2.threshold(image_np, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Convert back to PIL image
    processed_image = Image.fromarray(thresh_image)
    
    return processed_image

def minimal_preprocess(image):
    image = image.convert("L")  # Convert to grayscale
    width, height = image.size
    image = image.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
    return image


def clean_extracted_text(words: list) -> list:
    """Clean extracted text by removing common particles and unnecessary symbols."""
    arabic_particles = {
    "في", "من", "إلى", "على", "عن", "بـ", "كـ", "لـ", "حتى", "مذ", "منذ", "رُبَّ", "حاشا", "عدا", "خلا",
    "و", "ف", "ثم", "أو", "أم", "بل", "لا", "لكن", "إما", 
    "هل", "أ", "أين", "متى", "كيف", "ماذا", "من", "ما", "أي", "كم", 
    "لا", "ما", "لم", "لن", "ليس", "إن", "غير", "لولا", 
    "إنّ", "أن", "قد", "ل", "إلا", "سوى", "غير", 
    "يا", "أيا", "هيا", "أي", "آ", 
    "نعم", "بلى", "أجل", "كلا", "إي"
    }
    cleaned_words = [word for word in words if word not in arabic_particles]
    return cleaned_words

