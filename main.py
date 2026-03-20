from generator import generate_answer
from verifier import verify_answer
from rich.console import Console

console = Console()

def run_pipeline():
    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == 'exit':
            break

        result = generate_answer(query)
        console.print("[bold green]Generated Answer:[/bold green]")
        console.print(result['text'])

        verification = verify_answer(result['text'], query)
        console.print("[bold yellow]Verification:[/bold yellow]")
        console.print(verification)

if __name__ == "__main__":
    run_pipeline()