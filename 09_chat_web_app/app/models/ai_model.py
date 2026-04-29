import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class AIModel:
    """
    Wrapper around the Groq API for chat completions.

    Supports single-turn chat, multi-turn chat with history,
    and streaming responses.
    """

    def __init__(self, api_key=None, model=None):
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        self.model = model or os.getenv('GROQ_MODEL', 'llama3-8b-8192')

        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable not set.")

        self.client = Groq(api_key=self.api_key)

    def chat(self, message, system_prompt=None):
        """
        Single-turn chat with the AI model.

        Args:
            message (str): User message
            system_prompt (str, optional): System prompt override

        Returns:
            str: AI response text
        """
        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": message
        })

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                stream=False
            )
            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")

    def chat_with_history(self, messages):
        """
        Multi-turn chat using a pre-built message history.

        Args:
            messages (list): List of message dicts with 'role' and 'content'

        Returns:
            str: AI response text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                stream=False
            )
            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")

    def chat_stream(self, messages):
        """
        Streaming chat response generator.

        Args:
            messages (list): List of message dicts

        Yields:
            str: Individual content chunks from the stream
        """
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")

    def get_mode_info(self):
        """
        Return metadata about the current AI model configuration.

        Returns:
            dict: Model info
        """
        return {
            'model': self.model,
            'provider': 'Groq',
            'max_tokens': 2000
        }
