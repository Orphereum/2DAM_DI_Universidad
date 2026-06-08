from app.models.grupoInv import GrupoInvestigacion


class GrupoInvService:
    def __init__(self, grupoInv_repo):
        self.grupoInv_repo = grupoInv_repo

        # Contexto actual (si en el futuro filtras por algo)
        self.id_grupo_actual = None

    # -------------------------------------------------
    # CONTEXTO (opcional)
    # -------------------------------------------------
    def set_grupo_actual(self, id_grupo: int):
        self.id_grupo_actual = id_grupo

    # -------------------------------------------------
    # CONSULTAS
    # -------------------------------------------------
    def obtener_grupos(self):
        return self.grupoInv_repo.find_all()

    def obtener_grupo_por_id(self, id_grupo: int):
        return self.grupoInv_repo.find_by_id(id_grupo)

    # -------------------------------------------------
    # VALIDACIÓN
    # -------------------------------------------------
    def validar_grupo(self, grupo: GrupoInvestigacion):
        if not grupo.nombre or grupo.nombre.strip() == "":
            raise ValueError("El nombre del grupo es obligatorio")

        if not grupo.descripcion or grupo.descripcion.strip() == "":
            raise ValueError("La descripción es obligatoria")

        if grupo.fecha_creacion is None:
            raise ValueError("La fecha de creación es obligatoria")

    # -------------------------------------------------
    # CRUD
    # -------------------------------------------------
    def crear_grupo(self, grupo: GrupoInvestigacion):
        # Validación de duplicados
        if self.existe_grupo(grupo):
            raise ValueError("Ya existe un grupo con ese nombre")

        self.validar_grupo(grupo)
        return self.grupoInv_repo.insert(grupo)

    def actualizar_grupo(self, grupo: GrupoInvestigacion):
        if not grupo.id_grupo:
            raise ValueError("El grupo no tiene ID")

        self.validar_grupo(grupo)
        return self.grupoInv_repo.update(grupo)

    def eliminar_grupo(self, id_grupo: int):
        try:
            return self.grupoInv_repo.delete(id_grupo)
        except Exception:
            raise ValueError("No se puede eliminar el grupo (tiene relaciones)")

    # -------------------------------------------------
    # UTILIDAD
    # -------------------------------------------------
    def existe_grupo(self, grupo: GrupoInvestigacion):
        grupos = self.grupoInv_repo.find_all()

        for g in grupos:
            if g.nombre.strip().lower() == grupo.nombre.strip().lower():
                return True

        return False
