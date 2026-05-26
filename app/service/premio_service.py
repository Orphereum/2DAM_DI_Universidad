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

    def actualizar_premio(self, premio):
        if not premio.nombre_premio:
            raise ValueError("El nombre es obligatorio")
        if not premio.id_premio:
            raise ValueError("El premio no tiene ID")
        return self.repo.update(premio)

    def borrar_premio(self, id_premio):
        if not id_premio:
            raise ValueError("El ID es obligatorio")
        return self.repo.delete(id_premio)