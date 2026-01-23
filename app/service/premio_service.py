from app.repository.premio_repo import PremioRepository

class PremioService:
    def __init__(self):
        self.repo = PremioRepository()

    def obtener_premios(self):
        return self.repo.find_all()

    def crear_premio(self, premio):
        if not premio.nombre_premio:
            raise ValueError("El nombre es obligatorio")
        return self.repo.insert(premio)
    
    # ... resto de métodos CRUD