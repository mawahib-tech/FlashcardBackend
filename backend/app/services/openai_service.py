import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Make sure it's set in the environment variables.")

async def generate_flashcards(word):
    prompt = f"""
    أنت مساعد متخصص في علم الصرف في اللغة العربية الفصحى.
    الكلمة: {word}
    
    إذا كانت الكلمة فعل، أرجع الفعل الماضي، المضارع، المصدر، اسم الباب (مثل: ضَرَبَ يَضْرِبُ، نَصَرَ يَنْصُرُ)، وإذا كان الفعل غير منتظم (مثل: أجوف، ناقص، مثال، لفيف)، اذكر ذلك مع تحديد نوعه (واوي، يائي، همزة).
    
    إذا كانت الكلمة اسم، أرجع المفرد، المذكر والمؤنث، جميع صيغ الجمع، ومعنى الكلمة بالإنجليزية.
    
    قدم النتيجة بصيغة JSON فقط.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use gpt-4 for better accuracy
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        
        # Extract and parse the JSON response
        result = response['choices'][0]['message']['content']
        parsed_response = json.loads(result)
        
        # Format the response into front/back flashcards
        return format_flashcard(parsed_response)
        
    except Exception as e:
        return {"error": str(e)}

def format_flashcard(response):
    """Format the OpenAI response into a front/back flashcard structure."""
    if "past" in response:
        # It's a verb
        front = f"{response['past']} – {response['present']}\n{response['masdar']}\nباب: {response['bab']}"
        if "irregularity" in response:
            front += f"\nنوع الفعل: {response['irregularity']}"
        back = response["meaning"]
    else:
        # It's a noun
        plurals = ", ".join(response.get("plurals", []))
        front = f"{response['singular']}\nجمع: {plurals}"
        back = response["meaning"]
    
    return {"front": front, "back": back}
