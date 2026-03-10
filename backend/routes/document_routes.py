import os

from fastapi import APIRouter, HTTPException

from services import document_service

router = APIRouter()


@router.get('/documents')
def list_documents():

    sources = set()

    for chunk in document_service.DOCUMENT_CHUNKS:
        source = chunk.metadata.get('source')
        if source:
            sources.add(source)

    sorted_sources = sorted(sources)

    return {
        'documents': [
            {
                'name': os.path.basename(source),
                'source': source
            }
            for source in sorted_sources
        ],
        'total_documents': len(sorted_sources)
    }


@router.delete('/documents/{document_name:path}')
def remove_document(document_name: str):

    result = document_service.delete_document(document_name)

    if not result.get('deleted'):
        raise HTTPException(status_code=404, detail=result.get('detail', 'Document not found'))

    return result
