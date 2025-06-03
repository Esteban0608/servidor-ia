from transformers import pipeline

resumen = pipeline("summarization")
clasificacion = pipeline("sentiment-analysis")

def resumir_texto(texto: str) -> str:
    return resumen(texto, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]

def analizar_sentimiento(texto: str) -> str:
    return clasificacion(texto)[0]["label"]