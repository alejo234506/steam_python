"""Semana 4: primer servidor con FastAPI.

Ejecuta: python main.py   y abre http://127.0.0.1:8000/docs
"""

# 1. Importación de librerías
import uvicorn
from fastapi import FastAPI

# 2. Creación de la instancia
app = FastAPI(title="Mi primer servidor", version="1.0.0")


# 3. Hello world check
@app.get("/")
def hola_mundo() -> dict[str, str]:
    return {"mensaje": "Hola mundo 👋"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Ruta para comprobar que el servidor está vivo."""
    return {"estado": "ok"}


# 4. main == name: solo arranca el servidor si ejecutas este archivo directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
