from openai import OpenAI
from config import GROQ_API_KEY, VERIFY_MODEL, MAX_TOKENS

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def verify_answer(answer: str, prompt: str) -> str:
    verification_prompt = f"""
    You are a fact-checking assistant.
    User question: {prompt}
    Answer: {answer}

    Rate if the answer is likely correct:
    - 'CORRECT' or 'POSSIBLY INCORRECT' + short explanation.
    """

    response = client.responses.create(
        model=VERIFY_MODEL,
        input=verification_prompt,
        max_output_tokens=MAX_TOKENS,
    )
    return response.output_text