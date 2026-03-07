from fastapi import APIRouter
from services import document_service

router = APIRouter()


@router.get("/documents")
def list_documents():

    sources = set()

    for chunk in document_service.DOCUMENT_CHUNKS:
        source = chunk.metadata.get("source")
        if source:
            sources.add(source)

    return {
        "documents": list(sources),
        "total_documents": len(sources)
    }