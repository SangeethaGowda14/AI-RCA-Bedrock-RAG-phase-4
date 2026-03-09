def retrieve_logs(vector_store, query):
    """
    Simple fallback retrieval until vector search is added
    """
    try:
        docs = vector_store.documents
        return docs[:5]
    except:
        return []