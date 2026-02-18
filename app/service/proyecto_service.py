from app.models.proyecto import Proyecto
from app.repository.proyecto_repo import ProyectoRepository

class ProyectoService:
    
    def __init__(self, proyecto_repo):
        self.proyecto_repo = ProyectoRepository()
        
    def obtener_todos(self):
        return self.proyecto_repo.obtener_todos()