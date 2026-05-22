import unittest
from app.service.asignatura_service import AsignaturaService
from app.models.asignatura import Asignatura


# -------------------------
# MOCKS (simulamos repos)
# -------------------------

class MockAsignaturaRepo:
    def insert(self, asignatura):
        asignatura.id_asignatura = 1
        return asignatura

    def find_all_by_grado(self, id_grado):
        return []

    def update(self, asignatura):
        return asignatura

    def delete(self, id_asignatura):
        return True


class MockGradoRepo:
    def find_by_id(self, id_grado):
        return True  # simulamos que existe

    def find_all(self):
        return []


# -------------------------
# TESTS
# -------------------------

class TestAsignaturaService(unittest.TestCase):

    def setUp(self):
        self.service = AsignaturaService(
            MockAsignaturaRepo(),
            MockGradoRepo()
        )
        self.service.set_grado_actual(1)

    # ✅ TEST CREAR CORRECTO
    def test_crear_asignatura_ok(self):
        asignatura = Asignatura(
            id_asignatura=None,
            nombre="Matemáticas",
            creditos=6,
            curso=1,
            cuatrimestre=1,
            obligatoria=True,
            grado_fk=None
        )

        resultado = self.service.crear_asignatura(asignatura)

        self.assertIsNotNone(resultado.id_asignatura)
        self.assertEqual(resultado.nombre, "Matemáticas")

    # ❌ TEST ERROR NOMBRE VACÍO
    def test_crear_asignatura_sin_nombre(self):
        asignatura = Asignatura(
            id_asignatura=None,
            nombre="",
            creditos=6,
            curso=1,
            cuatrimestre=1,
            obligatoria=True,
            grado_fk=None
        )

        with self.assertRaises(ValueError):
            self.service.crear_asignatura(asignatura)

    # ❌ TEST CRÉDITOS INCORRECTOS
    def test_creditos_invalidos(self):
        asignatura = Asignatura(
            id_asignatura=None,
            nombre="Física",
            creditos=0,
            curso=1,
            cuatrimestre=1,
            obligatoria=True,
            grado_fk=None
        )

        with self.assertRaises(ValueError):
            self.service.crear_asignatura(asignatura)

    # ❌ TEST CURSO INVALIDO
    def test_curso_invalido(self):
        asignatura = Asignatura(
            id_asignatura=None,
            nombre="Química",
            creditos=6,
            curso=5,
            cuatrimestre=1,
            obligatoria=True,
            grado_fk=None
        )

        with self.assertRaises(ValueError):
            self.service.crear_asignatura(asignatura)


if __name__ == "__main__":
    unittest.main()