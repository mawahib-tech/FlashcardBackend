import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Load the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Make sure it's set in the environment variables.")


async def generate_flashcards(words):
    """Generate flashcard-style explanations for a list of words using OpenAI."""
    flashcards = {}
    
    for word in words:
        try:
            # Customize the prompt as needed
            response = openai.Completion.create(
                engine="text-davinci-003",  # Choose the appropriate model
                prompt=f"Provide a short definition or explanation for the Arabic word: {word}",
                max_tokens=50,
                temperature=0.7
            )
            explanation = response.choices[0].text.strip()
            flashcards[word] = explanation
        except Exception as e:
            flashcards[word] = f"Error: {e}"

    return flashcards