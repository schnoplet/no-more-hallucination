from openai import OpenAI
from config import GROQ_API_KEY, GEN_MODEL, MAX_TOKENS
from retriever import retrieve_docs

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def generate_answer(prompt: str) -> dict:
    context_docs = retrieve_docs(prompt)
    context = "\n\n".join(context_docs)
    full_prompt = f"Use the following documents to answer the question:\n{context}\n\nQuestion: {prompt}"

    response = client.responses.create(
        model=GEN_MODEL,
        input=full_prompt,
        max_output_tokens=MAX_TOKENS,
    )

    return {"text": response.output_text, "usage": getattr(response, 'usage', None)}