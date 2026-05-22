from datetime import datetime


class PublicacionService:
    def __init__(self, publicacion_repo):
        self.publicacion_repo = publicacion_repo

    def obtener_todos(self):
        return self.publicacion_repo.obtener_todos()

    def obtener_grupos_debate(self):
        return self.publicacion_repo.obtener_grupos_debate()

    def crear_publicacion(
        self,
        titulo,
        descripcion,
        fecha_publicacion,
        tipo,
        id_grupoDebate=None
    ):
        self._validar_publicacion(
            titulo,
            fecha_publicacion,
            id_grupoDebate
        )

        return self.publicacion_repo.crear_publicacion(
            titulo.strip(),
            descripcion.strip(),
            fecha_publicacion.strip(),
            tipo.strip(),
            id_grupoDebate
        )

    def actualizar_publicacion(
        self,
        id_publicacion,
        titulo,
        descripcion,
        fecha_publicacion,
        tipo,
        id_grupoDebate=None
    ):
        if id_publicacion is None:
            raise ValueError("Debes seleccionar una publicacion")

        self._validar_publicacion(
            titulo,
            fecha_publicacion,
            id_grupoDebate
        )

        self.publicacion_repo.actualizar_publicacion(
            id_publicacion,
            titulo.strip(),
            descripcion.strip(),
            fecha_publicacion.strip(),
            tipo.strip(),
            id_grupoDebate
        )

    def eliminar_publicacion(self, id_publicacion):
        if id_publicacion is None:
            raise ValueError("Debes seleccionar una publicacion")

        self.publicacion_repo.eliminar_publicacion(id_publicacion)

    def _validar_publicacion(
        self,
        titulo,
        fecha_publicacion,
        id_grupoDebate
    ):
        if not titulo or not titulo.strip():
            raise ValueError("El titulo es obligatorio")

        if fecha_publicacion and fecha_publicacion.strip():
            try:
                datetime.strptime(fecha_publicacion.strip(), "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError(
                    "La fecha debe tener formato yyyy-MM-dd"
                ) from exc

        if id_grupoDebate is not None:
            if not self.publicacion_repo.existe_grupo_debate(id_grupoDebate):
                raise ValueError("El grupo de debate seleccionado no existe")
