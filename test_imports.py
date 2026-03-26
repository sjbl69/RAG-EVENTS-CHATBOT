import sys

def test_faiss():
    try:
        import faiss
        print(" FAISS importé avec succès")
    except Exception as e:
        print(f" Erreur FAISS : {e}")
        return False
    return True


def test_langchain():
    try:
        from langchain_community.vectorstores import FAISS
        from langchain_community.embeddings import HuggingFaceEmbeddings
        print(" LangChain importé avec succès")
    except Exception as e:
        print(f" Erreur LangChain : {e}")
        return False
    return True


def test_mistral():
    try:
        import mistralai
        print(" Mistral importé avec succès")
    except Exception as e:
        print(f" Erreur Mistral : {e}")
        return False
    return True


def test_transformers():
    try:
        from sentence_transformers import SentenceTransformer
        print(" Sentence-Transformers importé avec succès")
    except Exception as e:
        print(f" Erreur Transformers : {e}")
        return False
    return True


def test_fastapi():
    try:
        from fastapi import FastAPI
        print(" FastAPI importé avec succès")
    except Exception as e:
        print(f" Erreur FastAPI : {e}")
        return False
    return True


if __name__ == "__main__":
    print(" Test des imports du projet RAG\n")

    results = [
        test_faiss(),
        test_langchain(),
        test_mistral(),
        test_transformers(),
        test_fastapi()
    ]

    print("\n Test terminé")

    if not all(results):
        sys.exit(1)