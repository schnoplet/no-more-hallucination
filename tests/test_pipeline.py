from generator import generate_answer
from verifier import verify_answer

def test_simple_query():
    query = "What is the capital of France?"
    answer = generate_answer(query)
    verification = verify_answer(answer['text'], query)
    assert "CORRECT" in verification or "correct" in verification.lower()