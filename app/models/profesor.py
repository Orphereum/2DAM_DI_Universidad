from dataclasses import dataclass, field


@dataclass
class Profesor:
    id: int = None
    nombre: str = None
    correo: str = None
    telefono: str = None
    titulo: str = None
    id_departamento: int = None
    jefe_dtp: bool = False
    asignaturas: list = field(default_factory=list)