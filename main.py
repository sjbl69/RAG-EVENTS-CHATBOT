from rag.chatbot import generate_answer


def main():
    print(" Chatbot événements (tape 'exit' pour quitter)\n")

    while True:
        query = input(" Ta question : ")

        if query.lower() == "exit":
            print(" À bientôt !")
            break

        try:
            answer = generate_answer(query)
            print("\n Réponse :")
            print(answer)
            print("\n" + "-"*50 + "\n")

        except Exception as e:
            print(f" Erreur : {e}")


if __name__ == "__main__":
    main()