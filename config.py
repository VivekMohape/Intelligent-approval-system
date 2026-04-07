import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PRIMARY_MODEL = "openai/oss-120b"
FALLBACK_MODEL = "llama3-8b-8192"
