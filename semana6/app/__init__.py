from fastapi import FastAPI

from app.config import settings
from app.routes import usuarios_router


def crear_app() -> FastAPI:
    """Fábrica de la aplicación: arma la app con su configuración y rutas."""
    app = FastAPI(title=settings.nombre_app, version=settings.version, debug=settings.debug)

    @app.get("/health", tags=["sistema"])
    def health_check() -> dict[str, str]:
        return {"estado": "ok", "version": settings.version}

    app.include_router(usuarios_router)
    return app


app = crear_app()
