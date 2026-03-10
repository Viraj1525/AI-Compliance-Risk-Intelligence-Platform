import re
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None


class LocalEmbeddingModel:
    """Lightweight embedding fallback when sentence-transformers is unavailable."""

    def __init__(self, dimension=384):
        self.dimension = dimension

    def encode(self, texts):
        vectors = []

        for text in texts:
            vec = np.zeros(self.dimension, dtype='float32')
            tokens = re.findall(r"[a-zA-Z0-9_]+", (text or '').lower())

            if not tokens:
                vectors.append(vec)
                continue

            for token in tokens:
                idx = hash(token) % self.dimension
                vec[idx] += 1.0

            norm = np.linalg.norm(vec)
            if norm > 0:
                vec = vec / norm

            vectors.append(vec.astype('float32'))

        return np.array(vectors, dtype='float32')


if SentenceTransformer is not None:
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    except Exception:
        model = LocalEmbeddingModel()
else:
    model = LocalEmbeddingModel()


def generate_embeddings(chunks):

    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(texts)

    return np.array(embeddings).astype('float32')
