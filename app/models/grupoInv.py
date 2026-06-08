from datetime import date

class GrupoInvestigacion:
    def __init__(
        self,
        id_grupo: int | None,
        nombre: str,
        descripcion: str,
        fecha_creacion: date
    ):
        self.id_grupo = id_grupo
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return f"{self.nombre} – creado el {self.fecha_creacion}"

    def to_tuple(self):
        """
        Devuelve los datos en formato tupla
        para inserts/updates en la BD.
        """
        return (
            self.nombre,
            self.descripcion,
            self.fecha_creacion
        )

