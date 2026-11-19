from fastapi import APIRouter, HTTPException, status

from app.schemas import Usuario, UsuarioCrear

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


class RepositorioUsuarios:
    """Guarda los usuarios en memoria. Cambiarlo por una base de datos
    no obliga a tocar las rutas: solo esta clase."""

    def __init__(self) -> None:
        self._datos: dict[int, Usuario] = {}
        self._siguiente_id = 1

    def listar(self) -> list[Usuario]:
        return list(self._datos.values())

    def obtener(self, usuario_id: int) -> Usuario | None:
        return self._datos.get(usuario_id)

    def email_en_uso(self, email: str, excepto_id: int | None = None) -> bool:
        return any(u.email == email and u.id != excepto_id for u in self._datos.values())

    def crear(self, datos: UsuarioCrear) -> Usuario:
        usuario = Usuario(id=self._siguiente_id, **datos.model_dump())
        self._datos[usuario.id] = usuario
        self._siguiente_id += 1
        return usuario

    def actualizar(self, usuario_id: int, datos: UsuarioCrear) -> Usuario:
        usuario = Usuario(id=usuario_id, **datos.model_dump())
        self._datos[usuario_id] = usuario
        return usuario

    def eliminar(self, usuario_id: int) -> bool:
        return self._datos.pop(usuario_id, None) is not None


repo = RepositorioUsuarios()


def _no_encontrado() -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


@router.get("/", response_model=list[Usuario])
def listar_usuarios() -> list[Usuario]:
    return repo.listar()


@router.get("/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int) -> Usuario:
    usuario = repo.obtener(usuario_id)
    if usuario is None:
        raise _no_encontrado()
    return usuario


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(datos: UsuarioCrear) -> Usuario:
    if repo.email_en_uso(datos.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya está registrado")
    return repo.crear(datos)


@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, datos: UsuarioCrear) -> Usuario:
    if repo.obtener(usuario_id) is None:
        raise _no_encontrado()
    if repo.email_en_uso(datos.email, excepto_id=usuario_id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya está registrado")
    return repo.actualizar(usuario_id, datos)


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int) -> None:
    if not repo.eliminar(usuario_id):
        raise _no_encontrado()
