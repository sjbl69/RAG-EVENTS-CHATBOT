from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

from rag.prompt import build_prompt


#  CONFIG

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not MISTRAL_API_KEY:
    raise ValueError(" MISTRAL_API_KEY non définie")

# embeddings 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


#  LOAD FAISS

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


#  CLIENT MISTRAL

client = MistralClient(api_key=MISTRAL_API_KEY)


#  RAG PIPELINE

def generate_answer(query: str) -> str:
    """
    Génère une réponse à partir du système RAG :
    1. Recherche FAISS
    2. Construction du contexte
    3. Prompt
    4. Appel Mistral
    """

    #  1. Recherche des documents pertinents
    docs = db.similarity_search(query, k=3)

    # fallback amélioré
    if not docs:
        return "Aucun événement trouvé pour votre recherche."

    #  2. Construction du contexte
    context_parts = []
    for doc in docs:
        text = doc.page_content

        # si metadata existe → bonus
        if doc.metadata:
            meta = doc.metadata
            text += f"\nLieu: {meta.get('location', 'Non précisé')}"
            text += f"\nDate: {meta.get('date', 'Non précisée')}"

        context_parts.append(text)

    context = "\n\n---\n\n".join(context_parts)

    #  3. Prompt
    prompt = build_prompt(context, query)

    #  4. Appel Mistral
    response = client.chat(
        model="mistral-small",
        messages=[ChatMessage(role="user", content=prompt)]
    )

    return response.choices[0].message.content