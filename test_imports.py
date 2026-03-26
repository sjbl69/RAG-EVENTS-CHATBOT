import sys

def test_faiss():
    import faiss

def test_langchain():
    from langchain_community.vectorstores import FAISS
    from langchain_community.embeddings import HuggingFaceEmbeddings

def test_mistral():
    import mistralai

def test_transformers():
    from sentence_transformers import SentenceTransformer

def test_fastapi():
    from fastapi import FastAPI


if __name__ == "__main__":
    print(" Test des imports du projet RAG\n")

    try:
        test_faiss()
        print(" FAISS OK")

        test_langchain()
        print(" LangChain OK")

        test_mistral()
        print(" Mistral OK")

        test_transformers()
        print(" Sentence-Transformers OK")

        test_fastapi()
        print(" FastAPI OK")

        print("\n Tous les imports sont fonctionnels")
        sys.exit(0)

    except Exception as e:
        print(f"\n ERREUR : {e}")
        sys.exit(1)