from pydantic import BaseModel, EmailStr, Field


class UsuarioBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=60, examples=["Ana Pérez"])
    email: EmailStr
    edad: int = Field(ge=0, le=120)


class UsuarioCrear(UsuarioBase):
    """Datos que llegan al crear o actualizar un usuario."""


class Usuario(UsuarioBase):
    """Usuario tal como lo devuelve la API."""

    id: int
