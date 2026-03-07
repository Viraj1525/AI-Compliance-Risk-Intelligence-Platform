from rag_pipeline.embeddings import model
from rag_pipeline.retriever import retrieve
from risk_engine.compliance_checker import analyze_compliance

from services import document_service


def chat_with_documents(question):

    if document_service.VECTOR_INDEX is None:
        return "No documents uploaded."

    query_embedding = model.encode([question])[0]

    results = retrieve(
        query_embedding,
        document_service.VECTOR_INDEX,
        document_service.DOCUMENT_CHUNKS,
        k=3
    )

    context = "\n".join([doc.page_content for doc in results])

    answer = analyze_compliance(context + "\n\nQuestion: " + question)

    return answer