from dataclasses import dataclass

@dataclass
class Edificio:
    id: int
    nombre: str
    id_facultad: int #Clave foranea de facultad    
