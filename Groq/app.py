# Name: Arav Shukla
# USN: 202510101110056
# Experiment: Groq API Call

import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Send request
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in simple terms."
        }
    ]
)

# Display response
print(response.choices[0].message.content)