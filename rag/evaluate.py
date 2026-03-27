def evaluate_answer(answer: str, expected: str) -> str:
    """
    Compare réponse IA avec réponse attendue
    """

    if answer.strip().lower() == expected.strip().lower():
        return "Exact Match"

    elif any(word in answer.lower() for word in expected.lower().split()):
        return "Partiellement correct"

    else:
        return "Incorrect"