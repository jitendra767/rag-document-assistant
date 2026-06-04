import tempfile

import streamlit as st

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embedding_model
from src.vectordb import create_vector_store
from src.retriever import retrieve_documents
from src.llm import generate_answer


st.set_page_config(
    page_title="RAG Document Assistant",
   
)

st.title(" RAG Document Assistant")

st.write("Upload a PDF and ask questions about it.")


# Session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file:

    if st.button("Process Document"):

        with st.spinner("Processing PDF..."):

            # Save uploaded PDF temporarily
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp_file:

                tmp_file.write(uploaded_file.read())
                pdf_path = tmp_file.name

            # Load PDF
            documents = load_pdf(pdf_path)

            # Chunking
            chunks = split_documents(documents)

            # Embeddings
            embedding_model = get_embedding_model()

            # FAISS
            vector_store = create_vector_store(
                chunks,
                embedding_model
            )

            st.session_state.vector_store = vector_store

        st.success("Document processed successfully!")


question = st.text_input(
    "Ask a question about the document"
)


if question and st.session_state.vector_store:

    with st.spinner("Searching document..."):

        docs = retrieve_documents(
            st.session_state.vector_store,
            question,
            k=5
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        answer = generate_answer(
            context,
            question
        )

    st.subheader("Answer")
    st.write(answer)