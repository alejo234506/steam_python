"""Menú de consola para administrar usuarios."""

from funciones_tarea import (
    actualizar_usuario,
    agregar_usuario,
    eliminar_usuario,
    visualizar_usuarios,
)

MENU = """
Seleccione una acción:
  1. Registrar usuario
  2. Actualizar usuario
  3. Eliminar usuario
  4. Visualizar usuarios
  x. Salir
"""


def programa(personas: list[str]) -> None:
    """Ejecuta el menú hasta que el usuario elija salir.

    Args:
        personas (list[str]): Lista de usuarios que se va a administrar.
    """
    while True:
        print("-" * 50)
        print(MENU)
        seleccion = input("Selección: ").strip().lower()

        if seleccion == "1":
            nombre = input("Nombre del usuario: ")
            if agregar_usuario(personas, nombre):
                print("[OK] Usuario registrado.")
            else:
                print("[!] El nombre está vacío o ya existe.")

        elif seleccion == "2":
            viejo = input("Usuario a actualizar: ")
            nuevo = input("Nuevo nombre: ")
            if actualizar_usuario(personas, viejo, nuevo):
                print("[OK] Usuario actualizado.")
            else:
                print("[!] No se pudo actualizar: revisa que exista y que el nuevo nombre sea válido.")

        elif seleccion == "3":
            nombre = input("Usuario a eliminar: ")
            if eliminar_usuario(personas, nombre):
                print("[OK] Usuario eliminado.")
            else:
                print("[!] Ese usuario no existe.")

        elif seleccion == "4":
            print(visualizar_usuarios(personas))

        elif seleccion == "x":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")
