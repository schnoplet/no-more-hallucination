import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GEN_MODEL = "openai/gpt-oss-20b"
VERIFY_MODEL = "openai/gpt-oss-6b"  # smaller, cheaper verification
CACHE_PATH = "./cache/"
MAX_TOKENS = 500
RETRIEVE_TOP_K = 3