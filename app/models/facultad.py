from dataclasses import dataclass

@dataclass
class Facultad:
    id_facultad: int
    id_universidad: int
    id_profesor: int
    nombre: str
    telefono: str
    email: str
    