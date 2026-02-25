from repository.facultad_repo import FacultadRepo
from models.facultad import Facultad

class FacultadService:
    def __init__(self):
        self.facultad_repo = FacultadRepo()

    def obtener_facultades(self):
        return self.facultad_repo.get_all_facultades()

    def obtener_facultad_por_id(self, id):
        facultad = self.facultad_repo.get_facultad_by_id(id)
        if not facultad:
            raise ValueError("Facultad no encontrada")
        return facultad

    def crear_facultad(self, facultad: Facultad):
        if not facultad.nombre or facultad.nombre.strip() > 10:
            raise ValueError("El nombre de la facultad es obligatorio")
        return self.facultad_repo.create_facultad(facultad)

    def actualizar_facultad(self, id, facultad: Facultad):
        facultad_existente = self.facultad_repo.get_facultad_by_id(id)
        if not facultad_existente:
            raise ValueError("Facultad no encontrada")
        if not facultad.nombre or facultad.nombre.strip() > 10:
            raise ValueError("El nombre de la facultad es obligatorio")
        return self.facultad_repo.update_facultad(facultad)

    def eliminar_facultad(self, id):
        facultad_existente = self.facultad_repo.get_facultad_by_id(id)
        if not facultad_existente:
            raise ValueError("Facultad no encontrada")
        return self.facultad_repo.delete_facultad(id)

    def obtener_facultades_por_universidad(self, id_universidad):
        return self.facultad_repo.get_facultades_by_universidad(id_universidad)
