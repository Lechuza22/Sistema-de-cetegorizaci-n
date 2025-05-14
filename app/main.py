# app/main.py

import os
from generate_embeddings import load_documents, create_vectorstore
from search_docs import buscar_documentos_relevantes
from generate_response import generar_respuesta_con_gemini

VECTOR_DIR = "vector_store"

# Crear índice si no existe
if not os.path.exists(VECTOR_DIR):
    print("[!] No se encontró el índice FAISS. Generándolo...")
    docs = load_documents()
    if docs:
        create_vectorstore(docs)
        print("[✓] Vectorstore generado correctamente.")
    else:
        print("[X] No se encontraron documentos válidos.")
        exit()

# Loop de consulta
while True:
    pregunta = input("\n🔍 Ingresá tu pregunta (o escribí 'salir'):\n> ")
    if pregunta.strip().lower() == "salir":
        break

    fragmentos = buscar_documentos_relevantes(pregunta)
    print("\n📄 Fragmentos relevantes:")
    for i, doc in enumerate(fragmentos, 1):
        print(f"[{i}] {doc.page_content[:250]}...\n")

    respuesta = generar_respuesta_con_gemini(pregunta, fragmentos)
    print("\n🧠 Respuesta generada por Gemini:")
    print(respuesta)
