from fastapi import FastAPI, UploadFile, File
from chatbot import responder_chat
from vision import describir_imagen
from text_analysis import resumir_texto, analizar_sentimiento
import shutil

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Servidor de IA activo"}

@app.post("/chat/")
def chat(user_input: str):
    respuesta = responder_chat(user_input)
    return {"respuesta": respuesta}

@app.post("/imagen/")
def imagen(file: UploadFile = File(...)):
    etiquetas = ["gato", "perro", "auto", "persona", "paisaje"]
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    resultado = describir_imagen(path, etiquetas)
    return {"etiqueta": resultado}

@app.post("/resumen/")
def resumen(texto: str):
    return {"resumen": resumir_texto(texto)}

@app.post("/sentimiento/")
def sentimiento(texto: str):
    return {"sentimiento": analizar_sentimiento(texto)}