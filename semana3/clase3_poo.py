"""Semana 3: objetos, clases abstractas, herencia, polimorfismo,
métodos especiales (funciones reservadas) y atributos privados.

Ejecuta: python clase3_poo.py
"""

from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    """Clase abstracta: define qué debe tener toda figura, sin implementarlo."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    @abstractmethod
    def area(self) -> float:
        """Cada figura calcula su área a su manera."""

    @abstractmethod
    def perimetro(self) -> float:
        """Cada figura calcula su perímetro a su manera."""

    # Funciones reservadas (métodos especiales)
    def __str__(self) -> str:
        return f"{self.nombre}: área {self.area():.2f}, perímetro {self.perimetro():.2f}"

    def __eq__(self, otra: object) -> bool:
        if not isinstance(otra, Figura):
            return NotImplemented
        return round(self.area(), 9) == round(otra.area(), 9)

    def __lt__(self, otra: "Figura") -> bool:
        return self.area() < otra.area()


class Rectangulo(Figura):
    """Herencia: un rectángulo ES una figura."""

    def __init__(self, base: float, altura: float) -> None:
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Cuadrado(Rectangulo):
    """Herencia en cadena: un cuadrado es un rectángulo con lados iguales."""

    def __init__(self, lado: float) -> None:
        super().__init__(lado, lado)
        self.nombre = "Cuadrado"


class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        super().__init__("Círculo")
        self.radio = radio

    def area(self) -> float:
        return pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * pi * self.radio


class CuentaAhorros:
    """Atributos y funciones privadas: el saldo solo cambia a través de métodos."""

    def __init__(self, titular: str) -> None:
        self.titular = titular
        self.__saldo = 0.0  # "privado": Python le cambia el nombre (name mangling)

    @property
    def saldo(self) -> float:
        """Permite leer el saldo, pero no asignarlo directamente."""
        return self.__saldo

    def depositar(self, monto: float) -> None:
        self.__validar(monto)
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        self.__validar(monto)
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= monto

    def __validar(self, monto: float) -> None:
        """Función privada: solo se usa dentro de la clase."""
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")


if __name__ == "__main__":
    # Polimorfismo: el mismo llamado (area, perimetro, str) se comporta
    # distinto según el tipo real de cada objeto.
    figuras: list[Figura] = [Rectangulo(3, 4), Cuadrado(2), Circulo(1.5)]
    for figura in figuras:
        print(figura)

    print("\nOrdenadas de menor a mayor área:")
    for figura in sorted(figuras):
        print(f"  {figura.nombre}")

    print("\n¿Un rectángulo 2x2 es igual a un cuadrado de lado 2?", Rectangulo(2, 2) == Cuadrado(2))

    cuenta = CuentaAhorros("Ana")
    cuenta.depositar(100_000)
    cuenta.retirar(30_000)
    print(f"\nSaldo de {cuenta.titular}: ${cuenta.saldo:,.0f}")

    try:
        Figura("genérica")  # type: ignore[abstract]
    except TypeError as error:
        print("\nNo se puede crear una Figura abstracta:", error)
