import sys
import os
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class RAGService:
    def ask(self, question: str) -> str:
        from rag.chatbot import generate_answer
        return generate_answer(question)

    def rebuild(self):
        result = subprocess.run(
            ["python", "scripts/build_vector_db.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise Exception(result.stderr)

        return result.stdout