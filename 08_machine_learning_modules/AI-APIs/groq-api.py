import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

def chat(user_message):
    """Send message and get response"""
    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        messages=[
            {
                "role":"system",
                "content":"You are a helpful AI Assistant"
            },
            {
                "role":"user",
                "content":user_message
            }
        ],
        max_tokens=1000,
        temperature=0.7
    )
    return response.choices[0].message.content

print(chat("What is python"))