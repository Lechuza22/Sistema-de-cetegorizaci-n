# app/generate_embeddings.py

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader

DATA_DIR = "data/documentos_raw"
VECTOR_DIR = "vectorstore"

def load_documents():
    documents = []
    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        if filename.endswith(".txt"):
            loader = TextLoader(path, autodetect_encoding=True)
        elif filename.endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            print(f"[!] Formato no compatible: {filename}")
            continue
        docs = loader.load()
        documents.extend(docs)
    return documents

def create_vectorstore(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_DIR)
    print(f"[✓] Vectorstore guardado en '{VECTOR_DIR}'")

if __name__ == "__main__":
    docs = load_documents()
    if docs:
        create_vectorstore(docs)
    else:
        print("[!] No se encontraron documentos válidos.")