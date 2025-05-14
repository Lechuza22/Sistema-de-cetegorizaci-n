# app/generate_response.py

import os
import requests
import json
from config import GEMINI_API_KEY

GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def generar_respuesta_con_gemini(pregunta, fragmentos):
    # Convertimos los documentos a texto plano
    contexto = "\n\n".join([doc.page_content for doc in fragmentos])

    prompt = f"""
Contexto:
{contexto}

Pregunta:
{pregunta}

Respondé de forma clara y directa usando solo la información del contexto si es posible.
"""

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(
        f"{GEMINI_ENDPOINT}?key={GEMINI_API_KEY}",
        headers=headers,
        data=json.dumps(body)
    )

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"[Error al interpretar la respuesta]: {e}"
    else:
        return f"[Error HTTP {response.status_code}]: {response.text}"
