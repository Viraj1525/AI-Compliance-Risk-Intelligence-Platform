import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from services.document_service import process_document

router = APIRouter()

UPLOAD_FOLDER = 'data/documents'
ALLOWED_EXTENSIONS = {'.pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post('/upload-document')
async def upload_document(file: UploadFile = File(...)):

    filename = os.path.basename(file.filename or '')

    if not filename:
        raise HTTPException(status_code=400, detail='Invalid filename')

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail='Only PDF documents are supported')

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = process_document(file_path)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f'Document processing failed: {str(exc)}') from exc

    return {
        'message': 'Document uploaded and processed successfully',
        'file': filename,
        'chunks_created': len(result['chunks'])
    }
