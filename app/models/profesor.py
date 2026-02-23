from dataclasses import dataclass

@dataclass
class Profesor:
    id: int = None
    nombre: str = None
    correo: str = None
    telefono: str = None
    titulo: str = None
    id_departamento: int = None
    jefe_dtp: bool = False
