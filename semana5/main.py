"""Semana 5: métodos HTTP, rutas dinámicas, router y schemas en FastAPI.

Ejecuta: python main.py   y abre http://127.0.0.1:8000/docs
"""

import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field


# ---------- Schemas ----------
class UsuarioCrear(BaseModel):
    nombre: str = Field(min_length=2, max_length=60, examples=["Ana Pérez"])
    email: EmailStr
    edad: int = Field(ge=0, le=120)


class Usuario(UsuarioCrear):
    id: int


# "Base de datos" en memoria para la práctica
usuarios: dict[int, Usuario] = {}
siguiente_id = 1

# ---------- Router ----------
router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("/", response_model=list[Usuario])
def listar_usuarios() -> list[Usuario]:
    return list(usuarios.values())


# Ruta dinámica: {usuario_id} cambia en cada petición
@router.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int) -> Usuario:
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios[usuario_id]


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(datos: UsuarioCrear) -> Usuario:
    global siguiente_id
    usuario = Usuario(id=siguiente_id, **datos.model_dump())
    usuarios[usuario.id] = usuario
    siguiente_id += 1
    return usuario


@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, datos: UsuarioCrear) -> Usuario:
    if usuario_id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuarios[usuario_id] = Usuario(id=usuario_id, **datos.model_dump())
    return usuarios[usuario_id]


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int) -> None:
    if usuarios.pop(usuario_id, None) is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


# ---------- App ----------
app = FastAPI(title="Clase 5 · Usuarios")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
