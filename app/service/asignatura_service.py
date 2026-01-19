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
        """
        Establece el grado activo sobre el que se trabaja.
        """
        self.id_grado_actual = id_grado

    # -------------------------------------------------
    # CONSULTAS
    # -------------------------------------------------
    def obtener_asignaturas(self):
        """
        Devuelve las asignaturas del grado actual.
        """
        if not self.id_grado_actual:
            return []

        return self.asignatura_repo.find_all_by_grado(
            self.id_grado_actual
        )

    def obtener_grados(self):
        """
        Devuelve los grados disponibles.
        SOLO lectura (no responsabilidad del módulo).
        """
        # Uso mínimo del repositorio de grado
        return self.grado_repo.find_all_by_facultad(1)

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

        # Validación cruzada (solo lectura)
        grado = self.grado_repo.find_by_id(asignatura.grado_fk)
        if not grado:
            raise ValueError("El grado seleccionado no existe")

    # -------------------------------------------------
    # CRUD
    # -------------------------------------------------
    def crear_asignatura(self, asignatura: Asignatura):
        """
        Valida y guarda una nueva asignatura.
        """
        self.validar_asignatura(asignatura)
        return self.asignatura_repo.insert(asignatura)

    def actualizar_asignatura(self, asignatura: Asignatura):
        """
        Valida y actualiza una asignatura existente.
        """
        if not asignatura.id_asignatura:
            raise ValueError("La asignatura no tiene ID")

        self.validar_asignatura(asignatura)
        return self.asignatura_repo.update(asignatura)

    def eliminar_asignatura(self, id_asignatura: int):
        """
        Elimina una asignatura por ID.
        """
        return self.asignatura_repo.delete(id_asignatura)
    
    
    def obtener_grados(self):
     try:
        return self.grado_repo.find_all_by_facultad(1)
     except Exception:
        # Fallback temporal mientras no exista la tabla
        from app.models.grado import Grado
        return [
            Grado(
                id_grado=1,
                nombre="Grado de prueba",
                codigo="G-TEST",
                duracion_anios=4,
                creditos_totales=240,
                tipo="Grado",
                estado=1,
                fecha_creacion=None,
                id_facultad=1
            )
        ]