import numpy as np


def retrieve(query_embedding, index, chunks, k=3):

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:

        if i < len(chunks):
            results.append(chunks[i])

    return results