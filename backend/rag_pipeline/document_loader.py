from dataclasses import dataclass


@dataclass
class SimpleDocument:
    page_content: str
    metadata: dict


def _load_with_langchain(file_path: str):
    from langchain_community.document_loaders import PyPDFLoader

    loader = PyPDFLoader(file_path)
    return loader.load()


def _load_with_pypdf(file_path: str):
    from pypdf import PdfReader

    reader = PdfReader(file_path)
    docs = []

    for page_no, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ''
        docs.append(
            SimpleDocument(
                page_content=text,
                metadata={'source': file_path, 'page': page_no}
            )
        )

    return docs


def load_pdf(file_path: str):
    """Load a PDF and return page-level documents with page_content/metadata."""

    try:
        return _load_with_langchain(file_path)
    except Exception:
        return _load_with_pypdf(file_path)
