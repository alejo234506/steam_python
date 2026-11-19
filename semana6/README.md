# CLASE 6
- Buenas practicas.
- entrypoint
- app
    - config.
    - routes.
    - schemas.

## Código
```
semana6/
├── entrypoint.py        arranca el servidor
└── app/
    ├── __init__.py      crea la app (crear_app)
    ├── config.py        configuración desde variables de entorno
    ├── routes/          rutas de la API
    └── schemas/         modelos de Pydantic
```

```bash
python entrypoint.py   # http://127.0.0.1:8000/docs
```

Variables opcionales: `APP_NOMBRE`, `APP_VERSION`, `APP_HOST`, `APP_PUERTO`, `APP_DEBUG`.
