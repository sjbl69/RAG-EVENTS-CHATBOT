from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Embeddings
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# Construction des documents + CHUNKING
def build_documents(events):
    documents = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for event in events:
        # compatibilité pipeline réel + tests
        text = event.get("text") or event.get("description", "")

        if not text:
            continue

        chunks = splitter.split_text(text)

        for chunk in chunks:
            # ✅ CORRECTION IMPORTANTE (alignement des données)
            metadata = {
                "title": event.get("title") or event.get("title_fr"),
                "date": event.get("date"),
                "location": event.get("location") or event.get("city"),
                "url": event.get("url"),
            }

            documents.append(
                Document(
                    page_content=chunk,
                    metadata=metadata
                )
            )

    return documents


# Création index FAISS
def create_faiss_index(documents):
    embeddings = get_embeddings()
    db = FAISS.from_documents(documents, embeddings)
    return db


# Sauvegarde index
def save_faiss(db, path="faiss_index"):
    db.save_local(path)


# Chargement index
def load_faiss(path="faiss_index"):
    embeddings = get_embeddings()
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )


# Recherche sémantique
def search(query, db, k=3):
    results = db.similarity_search(query, k=k)
    return results