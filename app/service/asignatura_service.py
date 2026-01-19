from app.models.asignatura import Asignatura
from app.models.grado import Grado


class AsignaturaService:
    """
    Servicio de negocio para Asignaturas.

    NOTA:
    - Actualmente usa datos simulados (fake) para Grados
    - Esto permite avanzar el desarrollo sin depender de la BD
    - Preparado para conectar a repositorio real más adelante
    """

    def __init__(self, grado_repo=None):
        # El repositorio se inyectará cuando la BD esté lista
        self.grado_repo = grado_repo

        # Datos FAKE de grados (temporal)
        self._grados_fake = [
            Grado(
                id_grado=1,
                nombre="Grado en Informática",
                codigo="GINF",
                duracion_anios=4,
                creditos_totales=240,
                tipo="Oficial",
                estado="Activo",
                fecha_creacion=None,
                id_facultad=1
            ),
            Grado(
                id_grado=2,
                nombre="Grado en Matemáticas",
                codigo="GMAT",
                duracion_anios=4,
                creditos_totales=240,
                tipo="Oficial",
                estado="Activo",
                fecha_creacion=None,
                id_facultad=1
            )
        ]

    # -------------------------
    # GRADOS PARA EL DIÁLOGO
    # -------------------------
    def obtener_grados(self):
        """
        Devuelve los grados disponibles.
        Actualmente usa datos simulados.
        """
        return self._grados_fake

    # -------------------------
    # VALIDACIÓN DE NEGOCIO
    # -------------------------
    def validar_asignatura(self, asignatura: Asignatura):
        if not asignatura.nombre:
            raise ValueError("El nombre es obligatorio")

        if asignatura.creditos <= 0:
            raise ValueError("Los créditos deben ser mayores que 0")

        if asignatura.curso not in (1, 2, 3, 4):
            raise ValueError("El curso debe estar entre 1 y 4")

        if asignatura.cuatrimestre not in (1, 2):
            raise ValueError("El cuatrimestre debe ser 1 o 2")

        # Validar grado contra datos fake
        if not any(g.id_grado == asignatura.grado_fk for g in self._grados_fake):
            raise ValueError("El grado seleccionado no existe")

    # -------------------------
    # CREAR ASIGNATURA
    # -------------------------
    def crear_asignatura(self, asignatura: Asignatura):
        """
        Valida y devuelve la asignatura.
        La persistencia se añadirá más adelante.
        """
        self.validar_asignatura(asignatura)
        return asignatura
