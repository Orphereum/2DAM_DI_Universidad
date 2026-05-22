from app.repository.grado_repo import GradoRepository
from app.models.grado import Grado


class GradoService:

    def __init__(self):
        self.repo = GradoRepository()

   
    # CONSULTAS

    def obtener_grados_por_facultad(self, id_facultad):
        if not id_facultad:
            raise ValueError("El id de la facultad es obligatorio")

        return self.repo.find_all_by_facultad(id_facultad)

    def obtener_grado_por_id(self, id_grado):
        grado = self.repo.find_by_id(id_grado)
        if not grado:
            raise ValueError("El grado no existe")
        return grado

    # CREAR

    def crear_grado(self, grado: Grado):
        self._validar_grado(grado)

        if not grado.id_facultad:
            raise ValueError("Un grado debe pertenecer a una facultad")

        return self.repo.insert(grado)

    # ACTUALIZAR

    def actualizar_grado(self, grado: Grado):
        if not grado.id_grado:
            raise ValueError("El id del grado es obligatorio para actualizar")

        existente = self.repo.find_by_id(grado.id_grado)
        if not existente:
            raise ValueError("No se puede actualizar un grado inexistente")

        self._validar_grado(grado)
        return self.repo.update(grado)
    
    
    # ELIMINAR
 

    def eliminar_grado(self, id_grado):
        if not id_grado:
            raise ValueError("El id del grado es obligatorio")

        grado = self.repo.find_by_id(id_grado)
        if not grado:
            raise ValueError("El grado no existe")

        return self.repo.delete(id_grado)


    # VALIDACIONES INTERNAS

    def _validar_grado(self, grado: Grado):
        if not grado.nombre or not grado.nombre.strip():
            raise ValueError("El nombre del grado es obligatorio")

        if not grado.codigo or not grado.codigo.strip():
            raise ValueError("El código del grado es obligatorio")

        if not grado.duracion_anios or grado.duracion_anios <= 0:
            raise ValueError("La duración del grado debe ser mayor que 0")

        if not grado.creditos_totales or grado.creditos_totales <= 0:
            raise ValueError("Los créditos totales deben ser mayores que 0")
