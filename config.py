import os

try:
    import streamlit as st
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    # fallback for local development (.env)
    from dotenv import load_dotenv
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Models
PRIMARY_MODEL = "openai/oss-120b"
FALLBACK_MODEL = "llama3-8b-8192"
