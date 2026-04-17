import os
from dotenv import load_dotenv

load_dotenv()



class APIConfig:
    """Some configurations about api and its model"""
    def __init__(self):

        self.api_key = os.getenv("MY_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1"
        self.model = 'llama-3.1-8b-instant'
        self.temperature = 0.7
        self.max_tokens = 1000

    