# Sistema-de-cetegorizaci-n
LLM Categorizer es una demo de asistente inteligente que responde preguntas en lenguaje natural usando documentos propios. Emplea FAISS para recuperar fragmentos relevantes y genera respuestas con Gemini 1.5 de Google. Ideal para soporte documental, educación o automatización de consultas.

# LLM Categorizer

**LLM Categorizer** es una demo funcional de un asistente inteligente que responde preguntas en lenguaje natural basándose en documentos propios. Utiliza embeddings semánticos con FAISS para recuperar fragmentos relevantes y genera respuestas precisas con el modelo Gemini 1.5 de Google. Ideal como base para sistemas de soporte documental, educación o automatización de consultas.

## Funcionalidad

- Procesa archivos `.txt` o `.pdf` ubicados en `data/documentos_raw/`
- Fragmenta y convierte los documentos en vectores con `HuggingFaceEmbeddings`
- Construye un índice de búsqueda semántica con FAISS
- Recibe una consulta del usuario en consola
- Recupera los fragmentos más relevantes
- Genera una respuesta con Gemini 1.5 (`gemini-2.0-flash`) vía API REST

## Uso local

1. Crear archivo `.env` con:

   ```
   GEMINI_API_KEY=tu_clave
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar:

   ```bash
   cd app
   python main.py
   ```

4. Escribir preguntas por consola

## Requisitos

- Python 3.10+
- Acceso a Gemini API (https://makersuite.google.com/app/apikey)
