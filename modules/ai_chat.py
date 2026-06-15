import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()                                        # Load variables from .env file
api_key = os.getenv("GEMINI_API_KEY")                # Read API key
genai.configure(api_key=api_key)                     # Configure Gemini
model = genai.GenerativeModel("gemini-2.5-flash")   # Create model object


def ask_ai(prompt):
    try:
        response = model.generate_content(f"Give a concise spoken response to: {prompt}")    #generate short response for speech
        return response.text

    except Exception as error:
        return f"Error: {error}"