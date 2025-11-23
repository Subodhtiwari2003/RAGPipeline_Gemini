import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.core.config import settings

CHROMA_PATH = "chroma_db"

def get_vectorstore():
    # Initialize Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    
    # Load Chroma from disk
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name="stock-data"
    )
    return vectorstore

def index_documents(chunks):
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    print("Documents indexed successfully.")# Handles Embeddings & ChromaDB
