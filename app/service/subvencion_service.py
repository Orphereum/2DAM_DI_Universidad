from app.models.subvencion import Subvencion

class SubvencionService:

    def __init__(self, subvencion_repo):
        self.subvencion_repo = subvencion_repo

    def obtener_todos(self):
        return self.subvencion_repo.obtener_todos()

    def crear_subvencion(self, nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado):
        return self.subvencion_repo.crear_subvencion(
            nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado
        )

    def actualizar_subvencion(self, id_subvencion, nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado):
        self.subvencion_repo.actualizar_subvencion(
            id_subvencion, nombre, importe_min, importe_max, fecha_inicio, fecha_fin, estado
        )

    def eliminar_subvencion(self, id_subvencion):
        self.subvencion_repo.eliminar_subvencion(id_subvencion)
