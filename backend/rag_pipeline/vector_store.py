import faiss
import numpy as np
import os

INDEX_PATH = "embeddings/faiss_index.bin"


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs("embeddings", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    return index


def load_faiss_index():

    if os.path.exists(INDEX_PATH):
        return faiss.read_index(INDEX_PATH)

    return None


def save_index(index):

    os.makedirs("embeddings", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)