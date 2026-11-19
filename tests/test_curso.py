"""Pruebas del curso. Ejecuta desde la raíz del repo:  python -m unittest -v"""

import importlib.util
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def cargar(nombre: str, ruta: Path):
    """Carga un archivo .py como módulo, aunque varias semanas usen el mismo nombre."""
    carpeta = str(ruta.parent)
    if carpeta not in sys.path:
        sys.path.insert(0, carpeta)
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


crud = cargar("funciones_tarea", RAIZ / "semana1" / "funciones_tarea.py")
geometria = cargar("function_s1", RAIZ / "semana1" / "function.py")
poo = cargar("clase3_poo", RAIZ / "semana3" / "clase3_poo.py")


class TestSemana1(unittest.TestCase):
    def test_agregar_rechaza_vacios_y_repetidos(self):
        datos: list[str] = []
        self.assertTrue(crud.agregar_usuario(datos, "  Ana "))
        self.assertFalse(crud.agregar_usuario(datos, "Ana"))
        self.assertFalse(crud.agregar_usuario(datos, "   "))
        self.assertEqual(datos, ["Ana"])

    def test_eliminar_inexistente_no_falla(self):
        datos = ["Ana"]
        self.assertFalse(crud.eliminar_usuario(datos, "Luis"))
        self.assertTrue(crud.eliminar_usuario(datos, "Ana"))
        self.assertEqual(datos, [])

    def test_actualizar_conserva_posicion(self):
        datos = ["Ana", "Luis", "Eva"]
        self.assertTrue(crud.actualizar_usuario(datos, "Luis", "Mario"))
        self.assertEqual(datos, ["Ana", "Mario", "Eva"])
        self.assertFalse(crud.actualizar_usuario(datos, "Nadie", "X"))
        self.assertFalse(crud.actualizar_usuario(datos, "Ana", "Eva"))

    def test_visualizar(self):
        self.assertEqual(crud.visualizar_usuarios([]), "No hay usuarios registrados.")
        self.assertEqual(crud.visualizar_usuarios(["Ana", "Luis"]), "1. Ana\n2. Luis")

    def test_area_rectangulo(self):
        self.assertEqual(geometria.area_rectangulo(3, 4), 12)
        with self.assertRaises(ValueError):
            geometria.area_rectangulo(0, 4)


class TestSemana3(unittest.TestCase):
    def test_polimorfismo(self):
        self.assertEqual(poo.Rectangulo(3, 4).area(), 12)
        self.assertEqual(poo.Cuadrado(2).perimetro(), 8)
        self.assertAlmostEqual(poo.Circulo(1).area(), 3.14159, places=4)

    def test_igualdad_y_orden(self):
        self.assertEqual(poo.Rectangulo(2, 2), poo.Cuadrado(2))
        self.assertLess(poo.Cuadrado(1), poo.Circulo(1))

    def test_clase_abstracta(self):
        with self.assertRaises(TypeError):
            poo.Figura("x")

    def test_cuenta_privada(self):
        cuenta = poo.CuentaAhorros("Ana")
        cuenta.depositar(100)
        cuenta.retirar(40)
        self.assertEqual(cuenta.saldo, 60)
        with self.assertRaises(ValueError):
            cuenta.retirar(1000)
        with self.assertRaises(ValueError):
            cuenta.depositar(-5)
        with self.assertRaises(AttributeError):
            cuenta.saldo = 999


try:
    from fastapi.testclient import TestClient
except ImportError:  # FastAPI no instalado: se omiten las pruebas de la API
    TestClient = None


@unittest.skipIf(TestClient is None, "Instala requirements.txt para probar las semanas 4 a 6")
class TestApis(unittest.TestCase):
    USUARIO = {"nombre": "Ana Pérez", "email": "ana@correo.com", "edad": 25}

    def test_semana4(self):
        app = cargar("main_s4", RAIZ / "semana4" / "main.py").app
        cliente = TestClient(app)
        self.assertEqual(cliente.get("/").status_code, 200)
        self.assertEqual(cliente.get("/health").json(), {"estado": "ok"})

    def _probar_crud(self, cliente, verificar_email_repetido: bool):
        r = cliente.post("/usuarios/", json=self.USUARIO)
        self.assertEqual(r.status_code, 201)
        uid = r.json()["id"]
        self.assertEqual(cliente.get(f"/usuarios/{uid}").json()["nombre"], "Ana Pérez")
        self.assertEqual(cliente.get("/usuarios/9999").status_code, 404)
        self.assertEqual(cliente.post("/usuarios/", json={**self.USUARIO, "edad": -1}).status_code, 422)
        self.assertEqual(cliente.post("/usuarios/", json={**self.USUARIO, "email": "no-es-email"}).status_code, 422)
        if verificar_email_repetido:
            self.assertEqual(cliente.post("/usuarios/", json=self.USUARIO).status_code, 409)
        r = cliente.put(f"/usuarios/{uid}", json={**self.USUARIO, "edad": 26})
        self.assertEqual(r.json()["edad"], 26)
        self.assertEqual(cliente.delete(f"/usuarios/{uid}").status_code, 204)
        self.assertEqual(cliente.delete(f"/usuarios/{uid}").status_code, 404)

    def test_semana5(self):
        app = cargar("main_s5", RAIZ / "semana5" / "main.py").app
        self._probar_crud(TestClient(app), verificar_email_repetido=False)

    def test_semana6(self):
        sys.path.insert(0, str(RAIZ / "semana6"))
        from app import crear_app

        cliente = TestClient(crear_app())
        self.assertEqual(cliente.get("/health").json()["estado"], "ok")
        self._probar_crud(cliente, verificar_email_repetido=True)


if __name__ == "__main__":
    unittest.main()
