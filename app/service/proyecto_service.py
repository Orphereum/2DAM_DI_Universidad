from app.models.proyecto import Proyecto


class ProyectoService:
    
    def __init__(self, proyecto_repo, subvencion_repo):
        self.proyecto_repo = proyecto_repo
        self.subvencion_repo = subvencion_repo
        
    def obtener_todos(self):
        return self.proyecto_repo.obtener_todos()
    
    def filtrar_por_grupo(self, id_grupo):
        return self.proyecto_repo.obtener_por_grupo(id_grupo)
    
    def obtener_subvenciones(self, id_proyecto):
        return self.proyecto_repo.obtener_subvenciones(id_proyecto)
    
    def crear_proyecto(self, nombre, descripcion, id_grupo):
        return self.proyecto_repo.crear_proyecto(nombre, descripcion, id_grupo)
    
    def obtener_por_grupo(self, id_grupo):
        return self.proyecto_repo.obtener_por_grupo(id_grupo)
    
    def actualizar_proyecto(self, id_proyecto, nombre, descripcion):
        self.proyecto_repo.actualizar_proyecto(id_proyecto, nombre, descripcion)
    
    def eliminar_proyecto(self, id_proyecto):
        self.proyecto_repo.eliminar_proyecto(id_proyecto)
    
    def obtener_proyecto_completo(self, id_proyecto):
        proyecto = self.proyecto_repo.obtener_por_id(id_proyecto)
        subvenciones = self.subvencion_repo.obtener_por_proyecto(id_proyecto)
        return proyecto, subvenciones
    
    def obtener_subvenciones_disponibles(self):
        return self.subvencion_repo.obtener_todos()

    def asignar_subvencion(self, id_proyecto, id_subvencion, importe):
        self.proyecto_repo.asignar_subvencion(id_proyecto, id_subvencion, importe)