"""Configuración de la aplicación, leída de variables de entorno."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    nombre_app: str = os.getenv("APP_NOMBRE", "Clase 6 · API de usuarios")
    version: str = os.getenv("APP_VERSION", "1.0.0")
    host: str = os.getenv("APP_HOST", "127.0.0.1")
    puerto: int = int(os.getenv("APP_PUERTO", "8000"))
    debug: bool = os.getenv("APP_DEBUG", "true").lower() == "true"


settings = Settings()
