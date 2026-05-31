from app.models.departamento import Departamento
from app.repository.departamento_repo import DepartamentoRepository
from app.repository.facultad_repo import FacultadRepo

class DepartamentoService:

    def __init__(self, departamento_repo=None, facultad_repo=None):
        self.departamento_repo = departamento_repo or DepartamentoRepository()
        self.facultad_repo = facultad_repo or FacultadRepo()

    def obtener_departamentos(self):
        return self.departamento_repo.find_all()

    def obtener_departamento_por_id(self, id_departamento: int):
        departamento = self.departamento_repo.find_by_id(id_departamento)
        if not departamento:
            raise ValueError("Departamento no encontrado")
        return departamento

    def obtener_departamentos_por_facultad(self, id_facultad: int):
        return self.departamento_repo.find_all_by_facultad(id_facultad)

    def obtener_facultades(self):
        return self.departamento_repo.find_all_facultades()

    def validar_departamento(self, departamento: Departamento):
        if not departamento.nombre or not departamento.nombre.strip():
            raise ValueError("El nombre del departamento es obligatorio")
        if departamento.id_facultad is None:
            raise ValueError("Debe seleccionar una facultad")

    def existe_departamento(self, departamento: Departamento):
        departamentos = self.departamento_repo.find_all_by_facultad(departamento.id_facultad)
        for d in departamentos:
            if departamento.id_departamento and d.id_departamento == departamento.id_departamento:
                continue
            if d.nombre.strip().lower() == departamento.nombre.strip().lower():
                return True
        return False

    def agregar(self, nombre: str, id_facultad: int):
        nuevo_departamento = Departamento(
            id_departamento=0,
            nombre=nombre,
            id_facultad=id_facultad,
            facultad=""
        )
        self.validar_departamento(nuevo_departamento)
        if self.existe_departamento(nuevo_departamento):
            raise ValueError("Este departamento ya existe en la facultad seleccionada")
        return self.departamento_repo.insert(nuevo_departamento)

    def editar(self, id_departamento: int, nombre: str, id_facultad: int):
        existente = self.departamento_repo.find_by_id(id_departamento)
        if not existente:
            raise ValueError("Departamento no encontrado")
        
        departamento_actualizado = Departamento(
            id_departamento=id_departamento,
            nombre=nombre,
            id_facultad=id_facultad,
            facultad=""
        )
        self.validar_departamento(departamento_actualizado)
        if self.existe_departamento(departamento_actualizado):
            raise ValueError("Este departamento ya existe en la facultad seleccionada")
        return self.departamento_repo.update(departamento_actualizado)

    def eliminar(self, id_departamento: int):
        existente = self.departamento_repo.find_by_id(id_departamento)
        if not existente:
            raise ValueError("Departamento no encontrado")
        try:
            return self.departamento_repo.delete(id_departamento)
        except Exception:
            raise ValueError("No se puede eliminar el departamento (tiene relaciones)")