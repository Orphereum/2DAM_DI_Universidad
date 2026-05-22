from dataclasses import dataclass
@dataclass

class Asignatura:
    def __init__(
        self,
        id_asignatura: int | None,
        nombre: str,
        creditos: int,
        curso: int,
        cuatrimestre: int,
        grado_fk: int, # Clave foranea perteneciente a la entidad de Grado
        obligatoria: bool
    ):
        self.id_asignatura = id_asignatura
        self.nombre = nombre
        self.creditos = creditos
        self.curso = curso
        self.cuatrimestre = cuatrimestre
        self.grado_fk = grado_fk
        self.obligatoria = obligatoria

    def __str__(self):
        return f"{self.nombre} ({self.creditos} ECTS)"

    def to_tuple(self):
        """
        Devuelve los datos en formato tupla
        para inserts/updates en la BD.
        """
        return (
            self.nombre,
            self.creditos,
            self.curso,
            self.cuatrimestre,
            self.grado_fk,
            int(self.obligatoria)
        )
