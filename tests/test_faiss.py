from data.vector_store import build_documents, create_faiss_index


def test_faiss_creation():
    events = [
        {
            "title": "Concert",
            "description": "Concert de musique classique à Lyon",
            "date": "2026-04-01",
            "location": "Lyon"
        }
    ]

    docs = build_documents(events)
    db = create_faiss_index(docs)

    assert db is not None