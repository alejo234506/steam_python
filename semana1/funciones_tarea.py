"""Operaciones CRUD sobre una lista de usuarios.

Las funciones no piden datos por consola: reciben lo que necesitan como
parámetros y devuelven el resultado. Así se pueden reutilizar y probar
fácilmente. La interacción con el usuario vive en ``programa.py``.
"""


def agregar_usuario(dataset: list[str], nombre: str) -> bool:
    """Agrega un usuario a la lista si no está vacío ni repetido.

    Args:
        dataset (list[str]): Lista de usuarios.
        nombre (str): Nombre del usuario a registrar.

    Returns:
        bool: True si se agregó, False si el nombre era vacío o ya existía.
    """
    nombre = nombre.strip()
    if not nombre or nombre in dataset:
        return False
    dataset.append(nombre)
    return True


def eliminar_usuario(dataset: list[str], nombre: str) -> bool:
    """Elimina un usuario de la lista.

    Args:
        dataset (list[str]): Lista de usuarios.
        nombre (str): Nombre del usuario a eliminar.

    Returns:
        bool: True si se eliminó, False si no existía.
    """
    nombre = nombre.strip()
    if nombre not in dataset:
        return False
    dataset.remove(nombre)
    return True


def actualizar_usuario(dataset: list[str], viejo: str, nuevo: str) -> bool:
    """Reemplaza un usuario por otro, conservando su posición en la lista.

    Args:
        dataset (list[str]): Lista de usuarios.
        viejo (str): Nombre actual del usuario.
        nuevo (str): Nombre nuevo.

    Returns:
        bool: True si se actualizó; False si ``viejo`` no existe,
        ``nuevo`` está vacío o ``nuevo`` ya está registrado.
    """
    viejo, nuevo = viejo.strip(), nuevo.strip()
    if viejo not in dataset or not nuevo or (nuevo != viejo and nuevo in dataset):
        return False
    dataset[dataset.index(viejo)] = nuevo
    return True


def visualizar_usuarios(dataset: list[str]) -> str:
    """Devuelve la lista de usuarios lista para imprimir.

    Args:
        dataset (list[str]): Lista de usuarios.

    Returns:
        str: Un usuario por línea, numerado, o un aviso si la lista está vacía.
    """
    if not dataset:
        return "No hay usuarios registrados."
    return "\n".join(f"{i}. {nombre}" for i, nombre in enumerate(dataset, start=1))
