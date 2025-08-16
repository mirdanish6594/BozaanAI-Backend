# services/llm_service.py
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_reply(transcript):
    """
    Generates a conversational reply in Kashmiri using the OpenAI API.
    """
    system_prompt = (
        "You are a helpful and friendly assistant who always replies in Kashmiri. "
        "Your user is speaking to you in Kashmiri, and you must respond naturally in the same language. "
        "Keep your replies concise and conversational."
    )
    
    user_prompt = f"The user said: '{transcript}'. Please reply in a casual tone in Kashmiri."

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating AI reply: {e}")
        return "Maaf kariv, me chu samkhun sapdun. (Sorry, I could not understand.)"