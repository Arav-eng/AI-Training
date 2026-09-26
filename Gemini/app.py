# Name: Arav Shukla
# USN: 202510101110056
# Experiment: Gemini API Call

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain artificial intelligence in simple terms."
)

print(response.text)