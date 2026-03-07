from document_loader import load_pdf
from text_splitter import split_documents
from embeddings import generate_embeddings
from vector_store import create_faiss_index

docs = load_pdf("../../data/documents/sample.pdf")

chunks = split_documents(docs)

embeddings = generate_embeddings(chunks)

index = create_faiss_index(embeddings)

print("Pipeline working successfully!")