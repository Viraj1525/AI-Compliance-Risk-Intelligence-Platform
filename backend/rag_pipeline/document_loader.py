from langchain_community.document_loaders import PyPDFLoader
import os


def load_pdf(file_path: str):
    """
    Load PDF document and return text pages
    """

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    return documents


if __name__ == "__main__":
    docs = load_pdf("../../data/documents/sample.pdf")

    for doc in docs[:2]:
        print(doc.page_content[:200])