from app.models.asignatura import Asignatura


class AsignaturaService:
    """
    Lógica de negocio del módulo Asignaturas.
    No contiene SQL.
    Valida datos y coordina repositorios.
    """

    def __init__(self, asignatura_repo, grado_repo):
        self.asignatura_repo = asignatura_repo
        self.grado_repo = grado_repo

        # Contexto actual (grado seleccionado)
        self.id_grado_actual = None

    # -------------------------------------------------
    # CONTEXTO
    # -------------------------------------------------
    def set_grado_actual(self, id_grado: int):
        self.id_grado_actual = id_grado

    # -------------------------------------------------
    # CONSULTAS
    # -------------------------------------------------
    def obtener_asignaturas(self):
        print("GRADO ACTUAL EN SERVICE:", self.id_grado_actual)
        if self.id_grado_actual is None:
            return []

        return self.asignatura_repo.find_all_by_grado(
            self.id_grado_actual
        )

    def obtener_grados(self):
        """
        🔥 Ahora carga TODOS los grados de la BD real
        """
        return self.grado_repo.find_all()

    # -------------------------------------------------
    # VALIDACIÓN
    # -------------------------------------------------
    def validar_asignatura(self, asignatura: Asignatura):
        if not asignatura.nombre:
            raise ValueError("El nombre es obligatorio")

        if asignatura.creditos <= 0:
            raise ValueError("Los créditos deben ser mayores que 0")

        if asignatura.curso not in (1, 2, 3, 4):
            raise ValueError("El curso debe estar entre 1 y 4")

        if asignatura.cuatrimestre not in (1, 2):
            raise ValueError("El cuatrimestre debe ser 1 o 2")

        if asignatura.grado_fk is None:
            raise ValueError("Debe seleccionar un grado")

        grado = self.grado_repo.find_by_id(asignatura.grado_fk)
        if not grado:
            raise ValueError("El grado seleccionado no existe")

    # -------------------------------------------------
    # CRUD
    # -------------------------------------------------
    def crear_asignatura(self, asignatura: Asignatura):
        """
        🔥 CLAVE: usa el grado seleccionado en la UI
        """
        if self.id_grado_actual is None:
            raise ValueError("No hay grado seleccionado")

        asignatura.grado_fk = self.id_grado_actual

        self.validar_asignatura(asignatura)
        return self.asignatura_repo.insert(asignatura)

    def actualizar_asignatura(self, asignatura: Asignatura):
        if not asignatura.id_asignatura:
            raise ValueError("La asignatura no tiene ID")

        if self.id_grado_actual is None:
            raise ValueError("No hay grado seleccionado")

        asignatura.grado_fk = self.id_grado_actual

        self.validar_asignatura(asignatura)
        return self.asignatura_repo.update(asignatura)

    def eliminar_asignatura(self, id_asignatura: int):
        try:
            return self.asignatura_repo.delete(id_asignatura)
        except Exception:
            raise ValueError(
                "No se puede eliminar la asignatura (tiene relaciones)"
            )