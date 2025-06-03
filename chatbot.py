import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def responder_chat(mensaje: str) -> str:
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": mensaje},
        ],
    )
    return respuesta.choices[0].message.content.strip()