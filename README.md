# RAG Document Assistant

## Overview

RAG Document Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content. The system retrieves relevant information from the uploaded document using semantic search and generates context-aware answers using a Large Language Model (LLM).

## Features

* Upload PDF documents
* Automatic document chunking
* Semantic search using embeddings
* FAISS vector database for retrieval
* Context-aware question answering
* OpenRouter LLM integration
* Streamlit-based user interface

## Tech Stack

* Python
* Streamlit
* LangChain
* Hugging Face Embeddings
* FAISS
* OpenRouter API
* OpenAI SDK
* PyPDF

## Architecture

PDF Upload

↓

Document Loading

↓

Text Chunking

↓

Embedding Generation

↓

FAISS Vector Store

↓

Similarity Search

↓

Context Retrieval

↓

LLM Response Generation

## Installation

```bash
git clone <repository-url>
cd rag-document-assistant

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

## Usage

1. Upload a PDF document.
2. Click Process Document.
3. Ask questions related to the uploaded document.
4. Receive context-aware answers generated from the document content.

## Future Improvements

* Multiple document support
* Chat history
* Persistent vector database
* Source citation display
* Advanced retrieval techniques
