def retrieve_logs(vector_store, query):
    return vector_store.search(query, k=3)