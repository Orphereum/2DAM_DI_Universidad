from dataclasses import dataclass

@dataclass
class Profesor:
    id_profesor: int
    nombre: str
    correo: str
    telefono: str
    titulo: str
    id_departamento: int #clave foránea de la entidad departamento
    jefe_dtp: bool #es jefe o lider  de departamento o no