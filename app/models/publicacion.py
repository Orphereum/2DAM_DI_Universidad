from dataclasses import dataclass


@dataclass
class Publicacion:
    id_publicacion: int | None
    titulo: str
    descripcion: str
    fecha_publicacion: str
    tipo: str
    id_grupoDebate: int | None = None
