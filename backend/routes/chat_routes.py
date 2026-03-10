from typing import List, Literal, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from services.chat_service import chat_with_documents

router = APIRouter()


class ChatHistoryItem(BaseModel):
    role: Literal['user', 'assistant']
    content: str


class ChatRequest(BaseModel):
    question: str
    history: Optional[List[ChatHistoryItem]] = None


@router.post('/chat')
def chat(request: ChatRequest):

    history_payload = []
    if request.history:
        history_payload = [
            {
                'role': item.role,
                'content': item.content,
            }
            for item in request.history
        ]

    response = chat_with_documents(request.question, history=history_payload)

    return {
        'answer': response
    }
