# 🤖 Servidor de Inteligencia Artificial (FastAPI)

Este proyecto es un servidor web con múltiples capacidades de IA integradas:

- 💬 Chatbot con OpenAI GPT
- 🖼️ Visión artificial con CLIP (OpenAI)
- 📝 Análisis de texto (resumen y sentimiento)

## 🚀 Requisitos

- Python 3.8+
- Cuenta en [OpenAI](https://platform.openai.com)
- Clave de API de OpenAI

## 📦 Instalación local

1. Clona el repositorio o descomprime el ZIP.
2. Crea un entorno virtual y activa:

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` o exporta tu clave de OpenAI:

```bash
export OPENAI_API_KEY=tu_clave
```

5. Ejecuta el servidor:

```bash
bash start.sh
```

Visita: [http://localhost:10000](http://localhost:10000)

---

## 🌐 Despliegue en Render

1. Sube este proyecto a un repositorio en GitHub.
2. Crea una cuenta en [https://render.com](https://render.com).
3. Crea un nuevo **Web Service** desde tu repo.
4. Llena la configuración:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `./start.sh`
   - **Environment:** Python 3
5. Agrega la variable de entorno:

```
KEY: OPENAI_API_KEY
VALUE: tu_clave
```

---

## 🧪 Endpoints disponibles

### `GET /`
Verifica que el servidor esté activo.

### `POST /chat/`
Chatbot con GPT

```json
{
  "user_input": "¿Qué es la inteligencia artificial?"
}
```

### `POST /imagen/`
Clasificación simple de imagen (usa etiquetas predefinidas)

**FormData:** imagen (`UploadFile`)

### `POST /resumen/`
Resumen de texto largo.

```json
{
  "texto": "Tu texto largo aquí..."
}
```

### `POST /sentimiento/`
Análisis de sentimiento.

```json
{
  "texto": "Estoy muy feliz hoy"
}
```

---

## 📄 Licencia

MIT