from dataclasses import dataclass


@dataclass
class GrupoDebate:
    id_grupo: int
    nombre: str
    tema_principal: str
    descripcion: str
    fecha_inicio: str
    estado: str