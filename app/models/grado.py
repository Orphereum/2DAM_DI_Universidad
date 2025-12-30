from dataclasses import dataclass
@dataclass
class Grado:
    def __init__(
        self,
        id_grado=None,
        nombre=None,
        codigo=None,
        duracion_anios=None,
        creditos_totales=None,
        tipo=None,
        estado=None,
        fecha_creacion=None,
        id_facultad=None
    ):
        self.id_grado = id_grado
        self.nombre = nombre
        self.codigo = codigo
        self.duracion_anios = duracion_anios
        self.creditos_totales = creditos_totales
        self.tipo = tipo
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.id_facultad = id_facultad
