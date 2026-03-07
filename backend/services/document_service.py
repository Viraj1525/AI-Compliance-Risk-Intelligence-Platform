import numpy as np
import pickle
import os

from rag_pipeline.document_loader import load_pdf
from rag_pipeline.text_splitter import split_documents
from rag_pipeline.embeddings import generate_embeddings
from rag_pipeline.vector_store import create_faiss_index, load_faiss_index, save_index


INDEX_PATH = "embeddings/faiss_index.bin"
CHUNKS_PATH = "embeddings/chunks.pkl"


VECTOR_INDEX = load_faiss_index()

# Load stored chunks if available
if os.path.exists(CHUNKS_PATH):
    with open(CHUNKS_PATH, "rb") as f:
        DOCUMENT_CHUNKS = pickle.load(f)
else:
    DOCUMENT_CHUNKS = []


def process_document(file_path):

    global VECTOR_INDEX
    global DOCUMENT_CHUNKS

    docs = load_pdf(file_path)

    chunks = split_documents(docs)

    for chunk in chunks:
        chunk.metadata["source"] = file_path

    embeddings = generate_embeddings(chunks)

    embeddings = np.array(embeddings).astype("float32")

    if VECTOR_INDEX is None:
        VECTOR_INDEX = create_faiss_index(embeddings)
    else:
        VECTOR_INDEX.add(embeddings)

    save_index(VECTOR_INDEX)

    DOCUMENT_CHUNKS.extend(chunks)

    # Save chunks
    os.makedirs("embeddings", exist_ok=True)
    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(DOCUMENT_CHUNKS, f)

    return {
        "chunks": chunks
    }