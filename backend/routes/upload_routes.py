from fastapi import APIRouter, UploadFile, File
import shutil
import os

from services.document_service import process_document

router = APIRouter()

UPLOAD_FOLDER = "data/documents"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # run RAG pipeline
    result = process_document(file_path)

    return {
        "message": "Document uploaded and processed successfully",
        "chunks_created": len(result["chunks"])
    }