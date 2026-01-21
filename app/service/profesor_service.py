from app.models.profesor import Profesor
from app.repository.profesor_repo import ProfesorRepository


class ProfesorService:

    def __init__(self, profesor_repo):
        self.profesor_repo = profesor_repo

    # consultas tipicas

    def obtener_profesores(self):
        return self.profesor_repo.find_all()


    # validacion y verificación

    def validar_profesor(self, profesor: Profesor):
        if not profesor.nombre or not profesor.nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if not profesor.correo or not profesor.correo.strip():
            raise ValueError("El correo es obligatorio")

        # validación simple
        if "@" not in profesor.correo:
            raise ValueError("El correo no es válido")

        if not profesor.telefono or not profesor.telefono.strip():
            raise ValueError("El teléfono es obligatorio")

        if not profesor.titulo or not profesor.titulo.strip():
            raise ValueError("El título es obligatorio")

        if profesor.id_departamento is None:
            raise ValueError("Debe seleccionar un departamento")


    # CRUD

    def crear_profesor(self, profesor: Profesor):
        self.validar_profesor(profesor)


        return self.profesor_repo.insert(profesor)

    def actualizar_profesor(self, profesor: Profesor):
        if not profesor.id:
            raise ValueError("El profesor no tiene ID")

        self.validar_profesor(profesor)


    def eliminar_profesor(self, id_profesor: int):
        return self.profesor_repo.delete(id_profesor)
