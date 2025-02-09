import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Function to generate flashcards
async def generate_flashcards(word: str) -> dict:
    prompt = f"""
    أنت مساعد متخصص في علم الصرف في اللغة العربية الفصحى.
    الكلمة: {word}

    إذا كانت الكلمة اسمًا، أرجع النتيجة بصيغة JSON تحتوي على:
    - جميع صيغ المفرد للكلمة في "singular_forms".
    - جميع صيغ الجمع للكلمة في "plural_forms".
    - معنى صيغة المفرد للكلمة بالإنجليزية في "meaning_english".

    إذا كانت الكلمة فعلًا، أرجع النتيجة بصيغة JSON تحتوي على:
    - "past" للفعل بصيغة الماضي.
    - "present" للفعل بصيغة المضارع.
    - "masdar" للفعل بصيغة المصدر.
    - "bab" اسم الباب:
      - للأفعال المجردة: (مثل: "ضَرَبَ يَضْرِبُ"، "فَتَحَ يَفْتَحُ").
      - للأفعال المزيدة: اسم الباب مثل (افتعال، استفعال، انفعال، تفعيل، تفعّل، تفاعل).
    - إذا كان الفعل غير منتظم، أرجع "irregularity" مع نوعه الكامل (مثل: "ناقص يائي"، "أجوف واوي"، "مثال همزة")، أو إذا كان الفعل منتظم، اجعلها "".

    إذا لم تكن الكلمة اسمًا أو فعلًا، أرجع النتيجة بصيغة JSON تحتوي على:
    - "singular_forms": ""
    - "plural_forms": ""
    - "meaning_english": ""
    """

    try:
        # Make request to OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",  # Use GPT-4 for better accuracy
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        
        # Extract and parse the JSON response
        result = response.choices[0].message.content
        parsed_response = json.loads(result)

        # Format the response into front/back flashcards
        return format_flashcard(parsed_response)
    except Exception as e:
        print(f"Error generating flashcards: {e}")
        return {}

# Helper function to format the response into flashcards
def format_flashcard(response):
    """Format the OpenAI response into front/back flashcard structure."""
    try:
        # Ensure necessary keys are present with defaults
        word_type = response.get("type", "n/a")

        if word_type == "verb":
            front = (
                f"{response.get('past', 'n/a')} – {response.get('present', 'n/a')}\n"
                f"{response.get('masdar', 'n/a')}\n"
                f"باب: {response.get('bab', 'n/a')}"
            )
            irregularity = response.get("irregularity")
            if irregularity:
                front += f"\nنوع الفعل: {irregularity}"
            back = response.get("meaning_english", "No meaning available")

        elif word_type == "noun":
            plurals = ", ".join(response.get("plural_forms", []))
            front = f"{response.get('singular_forms', 'n/a')}\nجمع: {plurals or 'n/a'}"
            back = response.get("meaning_english", "No meaning available")

        else:  # Handle "n/a" case
            front = "n/a"
            back = "n/a"

        return {"flashcards": [{"front": front, "back": back}]}

    except Exception as e:
        return {"error": f"Failed to format flashcard: {str(e)}"}