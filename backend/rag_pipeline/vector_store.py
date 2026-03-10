import os
import pickle

import numpy as np

try:
    import faiss
except Exception:
    faiss = None

INDEX_PATH = 'embeddings/faiss_index.bin'


class NumpyIndex:
    """Simple in-memory vector index fallback used when FAISS is unavailable."""

    def __init__(self, vectors=None):
        if vectors is None:
            self.vectors = np.empty((0, 0), dtype='float32')
        else:
            self.vectors = np.array(vectors).astype('float32')

    def add(self, embeddings):
        embeddings = np.array(embeddings).astype('float32')

        if embeddings.size == 0:
            return

        if self.vectors.size == 0:
            self.vectors = embeddings
            return

        self.vectors = np.vstack([self.vectors, embeddings])

    def search(self, query_embedding, k):
        query = np.array(query_embedding).astype('float32')

        if query.ndim == 1:
            query = np.array([query], dtype='float32')

        if self.vectors.size == 0:
            distances = np.full((query.shape[0], k), np.inf, dtype='float32')
            indices = np.full((query.shape[0], k), -1, dtype='int64')
            return distances, indices

        dists = ((self.vectors[None, :, :] - query[:, None, :]) ** 2).sum(axis=2)
        top_idx = np.argsort(dists, axis=1)[:, :k]
        top_dist = np.take_along_axis(dists, top_idx, axis=1)

        return top_dist.astype('float32'), top_idx.astype('int64')


def create_faiss_index(embeddings):

    embeddings = np.array(embeddings).astype('float32')

    os.makedirs('embeddings', exist_ok=True)

    if faiss is not None:
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)
        faiss.write_index(index, INDEX_PATH)
        return index

    index = NumpyIndex(embeddings)
    with open(INDEX_PATH, 'wb') as handle:
        pickle.dump({'type': 'numpy', 'vectors': index.vectors}, handle)
    return index


def load_faiss_index():

    if not os.path.exists(INDEX_PATH):
        return None

    if faiss is not None:
        try:
            return faiss.read_index(INDEX_PATH)
        except Exception:
            pass

    try:
        with open(INDEX_PATH, 'rb') as handle:
            payload = pickle.load(handle)
        if isinstance(payload, dict) and payload.get('type') == 'numpy':
            return NumpyIndex(payload.get('vectors'))
    except Exception:
        return None

    return None


def save_index(index):

    os.makedirs('embeddings', exist_ok=True)

    if faiss is not None and not isinstance(index, NumpyIndex):
        faiss.write_index(index, INDEX_PATH)
        return

    vectors = getattr(index, 'vectors', np.empty((0, 0), dtype='float32'))
    with open(INDEX_PATH, 'wb') as handle:
        pickle.dump({'type': 'numpy', 'vectors': vectors}, handle)
