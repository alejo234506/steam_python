def area_rectangulo(altura: float, base: float) -> float:
    """Calcula el área de un rectángulo.

    Args:
        altura (float): Altura del rectángulo. Debe ser mayor que cero.
        base (float): Base del rectángulo. Debe ser mayor que cero.

    Returns:
        float: El área del rectángulo.

    Raises:
        ValueError: Si la altura o la base no son positivas.
    """
    if altura <= 0 or base <= 0:
        raise ValueError("La altura y la base deben ser mayores que cero.")
    return altura * base


def pedir_numero(mensaje: str) -> float:
    """Pide un número positivo por consola hasta que sea válido."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Escribe un número válido.")
            continue
        if valor > 0:
            return valor
        print("El número debe ser mayor que cero.")


if __name__ == "__main__":
    altura = pedir_numero("Ingrese la altura del rectángulo: ")
    base = pedir_numero("Ingrese la base del rectángulo: ")
    print(f"El área es {area_rectangulo(altura, base)}")
