from dataclasses import dataclass

@dataclass
class Clase:
    id_clase: int | None  
    nombre: str
    capacidad: int        
    id_edificio: int      # Clave foránea

    def to_tuple(self):
        """Para insertar/actualizar en BD"""
        return (self.nombre, self.capacidad, self.id_edificio)