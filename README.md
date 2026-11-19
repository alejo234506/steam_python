# 🐍 Clases de Python

Curso práctico de Python: desde buenas prácticas y programación orientada a objetos hasta crear una API con FastAPI.

![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic_v2-E92063?style=flat-square&logo=pydantic&logoColor=white)

## 📅 Contenido

| Semana | Tema | Código |
|--|--|--|
| [1](semana1/README.md) | Repaso y buenas prácticas: tipado, docstrings, módulos, `__main__` | `function.py`, `entrypoint.py`, CRUD de usuarios en `tarea_semana1.py` |
| [2](semana2/README.md) | Introducción a clases: constantes, parámetros, `__str__`, métodos | `clase2_*.py` |
| [3](semana3/README.md) | POO: clases abstractas, herencia, polimorfismo, métodos especiales y privados | `clase3_poo.py` |
| [4](semana4/README.md) | Primer servidor con FastAPI | `main.py` |
| [5](semana5/README.md) | Métodos HTTP, rutas dinámicas, router y schemas | `main.py` |
| [6](semana6/README.md) | Buenas prácticas: proyecto organizado en `config`, `routes` y `schemas` | `entrypoint.py` + `app/` |

## 🚀 Cómo usarlo

```bash
# 1. Crear y activar un entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS

# 2. Instalar dependencias (necesarias desde la semana 4)
pip install -r requirements.txt
```

Ejemplos:

```bash
cd semana1 && python tarea_semana1.py   # menú de usuarios por consola
cd semana3 && python clase3_poo.py      # figuras, herencia y polimorfismo
cd semana5 && python main.py            # API → http://127.0.0.1:8000/docs
cd semana6 && python entrypoint.py      # API organizada → http://127.0.0.1:8000/docs
```

## ✅ Pruebas

Desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
```

Las pruebas de las semanas 1 y 3 solo necesitan Python. Las de las semanas 4 a 6 se ejecutan si instalaste `requirements.txt` (si no, se omiten).

## 📁 Estructura

```
steam_python/
├── semana1/   buenas prácticas + CRUD por consola
├── semana2/   introducción a clases
├── semana3/   programación orientada a objetos
├── semana4/   primer servidor FastAPI
├── semana5/   rutas, router y schemas
├── semana6/   proyecto organizado
│   ├── entrypoint.py
│   └── app/
│       ├── config.py
│       ├── routes/
│       └── schemas/
├── tests/
└── requirements.txt
```

---

Basado en el curso de [Felipeagq/steam_python](https://github.com/Felipeagq/steam_python).
