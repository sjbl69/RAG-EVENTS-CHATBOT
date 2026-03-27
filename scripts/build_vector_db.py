from data.collect_events import fetch_events, clean_events
from data.vector_store import build_documents, create_faiss_index, save_faiss

print(" Fetch events...")
events = fetch_events()

print(" Clean events...")
cleaned = clean_events(events)

print(" Build documents...")
documents = build_documents(cleaned)

print(" Create FAISS index...")
db = create_faiss_index(documents)

print(" Save index...")
save_faiss(db)

print(" DONE")