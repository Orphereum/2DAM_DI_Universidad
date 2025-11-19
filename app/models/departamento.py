from dataclasses import dataclass

@dataclass
class Departamento:
    id_departamento: int 
    nombre: str
    facultad: str 
    id_facultad: int #clave foranea de facultad