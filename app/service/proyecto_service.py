from app.models.proyecto import Proyecto


class ProyectoService:
    
    def __init__(self, proyecto_repo):
        self.proyecto_repo = proyecto_repo
        
    def obtener_todos(self):
        return self.proyecto_repo.obtener_todos()
    
    def filtrar_por_grupo(self, id_grupo):
        return self.proyecto_repo.obtener_por_grupo(id_grupo)
    
    def obtener_subvenciones(self, id_proyecto):
        return self.proyecto_repo.obtener_subvenciones(id_proyecto)