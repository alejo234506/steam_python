"""Punto de entrada de la API de la semana 6.

Ejecuta desde la carpeta semana6:  python entrypoint.py
y abre http://127.0.0.1:8000/docs
"""

import uvicorn

from app.config import settings

if __name__ == "__main__":
    uvicorn.run("app:app", host=settings.host, port=settings.puerto, reload=settings.debug)
