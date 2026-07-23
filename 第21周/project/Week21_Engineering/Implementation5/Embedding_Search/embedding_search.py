from src.Implementation4.vector_search import vector_search


def embedding_search(query, k=5):
    return vector_search(query, k=k)


def search2(query, k=5):
    return embedding_search(query, k=k)
