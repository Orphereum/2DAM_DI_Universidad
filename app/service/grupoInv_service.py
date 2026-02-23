from app.models.grupoInv import GrupoInvestigacion
from app.repository.grupoInv_repo import GrupoInvRepository

class GrupoInvService:
    
    def __init__(self, grupoInv_repo):
        self.grupoInv_repo = grupoInv_repo
    
    def cargar_lista_gruposInv(self):
        return self.grupoInv_repo.cargar_lista_gruposInv()