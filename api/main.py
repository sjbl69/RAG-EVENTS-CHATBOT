from fastapi import FastAPI, HTTPException
from api.schemas import QuestionRequest, AnswerResponse
from api.rag_service import RAGService
import traceback

app = FastAPI(title="RAG Events API")

rag_service = RAGService()


@app.get("/")
def root():
    return {"message": "RAG API is running"}


# ASK ENDPOINT

@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question vide")

    try:
        answer = rag_service.ask(request.question)
        return {"answer": answer}

    except Exception as e:
        print("\n ERREUR /ask ")
        traceback.print_exc()
        return {"error": str(e)}


#  REBUILD ENDPOINT

@app.post("/rebuild")
def rebuild_index():
    try:
        result = rag_service.rebuild()
        return {
            "message": "Base vectorielle reconstruite",
            "details": result
        }

    except Exception as e:
        print("\n ERREUR /rebuild ")
        traceback.print_exc()
        return {"error": str(e)}