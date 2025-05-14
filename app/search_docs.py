# app/search_documents.py

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # este era el que faltaba

VECTOR_DIR = "vectorstore"

def load_vectorstore():
    if not os.path.exists(VECTOR_DIR):
        raise FileNotFoundError("[!] No se encontró el vectorstore. Ejecutá generate_embeddings.py primero.")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)

def buscar_documentos_relevantes(pregunta, k=3):
    vectorstore = load_vectorstore()
    resultados = vectorstore.similarity_search(pregunta, k=k)
    return resultados
