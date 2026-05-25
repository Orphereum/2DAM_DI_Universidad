from app.models.grupo_debate import GrupoDebate


class GrupoDebateService:

    def __init__(self, grupo_debate_repo):
        self.grupo_debate_repo = grupo_debate_repo

    def obtener_todos(self):
        return self.grupo_debate_repo.obtener_todos()

    def crear_grupo(
        self,
        nombre,
        tema_principal,
        descripcion,
        fecha_inicio,
        estado
    ):

        return self.grupo_debate_repo.crear_grupo(
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado
        )

    def actualizar_grupo(
        self,
        id_grupo,
        nombre,
        tema_principal,
        descripcion,
        fecha_inicio,
        estado
    ):

        self.grupo_debate_repo.actualizar_grupo(
            id_grupo,
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado
        )

    def eliminar_grupo(self, id_grupo):

        self.grupo_debate_repo.eliminar_grupo(
            id_grupo
        )