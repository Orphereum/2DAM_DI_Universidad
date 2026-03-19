from dataclasses import dataclass

@dataclass
class Facultad:
    id: int
    id_universidad: int #Foreign Key to Universidad
    id_profesor: int #Foreign Key to Profesor
    nombre: str
    telefono: str
    email: str
    