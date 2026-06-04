def retrieve_documents(
    vector_store,
    query,
    k=5
):
    """
    Retrieve relevant chunks from FAISS.
    """

    docs = vector_store.similarity_search(
        query,
        k=k
    )

    return docs