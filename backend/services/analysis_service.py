from rag_pipeline.embeddings import model
from rag_pipeline.retriever import retrieve
from risk_engine.compliance_checker import analyze_compliance
from risk_engine.risk_scoring import calculate_compliance_score

from services import document_service


def run_analysis(query):

    # Check if documents exist
    if document_service.VECTOR_INDEX is None:
        return {
            "analysis": "No documents uploaded yet.",
            "compliance_score": 0
        }

    # Convert query to embedding
    query_embedding = model.encode([query])[0]

    # Retrieve relevant chunks
    results = retrieve(
        query_embedding,
        document_service.VECTOR_INDEX,
        document_service.DOCUMENT_CHUNKS
    )

    # Build context with document sources
    context_parts = []

    for doc in results:

        source = doc.metadata.get("source", "unknown")

        text = doc.page_content

        context_parts.append(
            f"Document: {source}\n{text}"
        )

    context = "\n\n".join(context_parts)

    # Run LLM analysis
    analysis = analyze_compliance(context)

    # Calculate compliance score
    score = calculate_compliance_score(analysis)

    return {
        "analysis": analysis,
        "compliance_score": score
    }