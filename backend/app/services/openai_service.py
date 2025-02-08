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
    """Generate flashcard-style explanations using OpenAI's chat-based API."""
    flashcards = {}

    for word in words:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the chat-based model
                messages=[
                    {"role": "system", "content": "You are an assistant that provides short definitions or explanations for Arabic words."},
                    {"role": "user", "content": f"Provide a short definition or explanation for the Arabic word: {word}"}
                ],
                temperature=0.7,
                max_tokens=50
            )
            explanation = response['choices'][0]['message']['content'].strip()
            flashcards[word] = explanation
        except Exception as e:
            flashcards[word] = f"Error: {e}"

    return flashcards