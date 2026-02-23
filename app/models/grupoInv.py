from dataclasses import dataclass
from datetime import date


@dataclass
class GrupoInvestigacion:
    id_grupo: int
    nombre: str
    descripcion: str
    fecha_creacion: date
