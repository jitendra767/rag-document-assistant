from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Create FAISS vector database from document chunks.
    """

    vector_store = FAISS.from_documents(
        chunks,
        embedding_model
    )

    return vector_store


def save_vector_store(
    vector_store,
    path="vectorstore"
):
    """
    Save FAISS database locally.
    """

    vector_store.save_local(path)


def load_vector_store(
    embedding_model,
    path="vectorstore"
):
    """
    Load existing FAISS database.
    """

    vector_store = FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store