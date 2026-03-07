from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import chat_with_documents

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    response = chat_with_documents(request.question)

    return {
        "answer": response
    }