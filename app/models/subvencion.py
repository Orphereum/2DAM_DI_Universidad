from dataclasses import dataclass

@dataclass
class Subvencion:
    id_subvencion: int
    nombre_subvencion: str
    importe_minimo: float
    importe_maximo: float
    fecha_inicio: str
    fecha_final: str
    estado_subvencion: str