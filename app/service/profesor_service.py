from app.models.profesor import Profesor


class ProfesorService:

    def __init__(self, profesor_repo):
        self.profesor_repo = profesor_repo

    # CONSULTAS
    def obtener_profesores(self):
        return self.profesor_repo.find_all()

    def obtener_profesor_por_id(self, id_profesor):
        profesor = self.profesor_repo.find_by_id(id_profesor)
        if not profesor:
            raise ValueError("El profesor no existe")
        return profesor

    def obtener_profesores_por_departamento(self, id_departamento):
        if not id_departamento:
            raise ValueError("El id del departamento es obligatorio")
        return self.profesor_repo.find_by_departamento(id_departamento)

    # VALIDACIÓN
    def validar_profesor(self, profesor: Profesor):
        if not profesor.nombre or not profesor.nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if not profesor.correo or not profesor.correo.strip():
            raise ValueError("El correo es obligatorio")

        if "@" not in profesor.correo:
            raise ValueError("El correo no es válido")

        if not profesor.telefono or not profesor.telefono.strip():
            raise ValueError("El teléfono es obligatorio")

        if not profesor.titulo or not profesor.titulo.strip():
            raise ValueError("El título es obligatorio")

        # sin repo de departamento por ahora:
        if profesor.id_departamento is None:
            raise ValueError("Debe seleccionar un departamento")

    # CRUD
    def crear_profesor(self, profesor: Profesor):
        self.validar_profesor(profesor)

        if profesor.jefe_dtp:
            self.profesor_repo.desmarcar_jefes_del_departamento(profesor.id_departamento)

        return self.profesor_repo.insert(profesor)

    def actualizar_profesor(self, profesor: Profesor):
        if not profesor.id:
            raise ValueError("El profesor no tiene ID")

        self.validar_profesor(profesor)

        if profesor.jefe_dtp:
            self.profesor_repo.desmarcar_jefes_del_departamento(profesor.id_departamento)

        return self.profesor_repo.update(profesor)

    def eliminar_profesor(self, id_profesor: int):
        return self.profesor_repo.delete(id_profesor)
