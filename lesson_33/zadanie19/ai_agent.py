from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()

client = genai.Client()

async def generate_response(prompt: str, model_name: str = "gemini-2.5-flash") -> str:
    try:
        response = await client.aio.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Błąd Gemini API: {e}")
        raise e