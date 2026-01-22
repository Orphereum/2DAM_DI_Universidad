from app.models.edificio import Edificio


class EdificioService:

    def __init__(self, edificio_repo, facultad_repo):
        self.edificio_repo = edificio_repo
        self.facultad_repo = facultad_repo



    # CONSULTAS
    
    #TODO: TERMINAR CUANDO FACULTAD REPO ESTÉ COMPLETO
    
    def obtener_edificios(self):
        return self.edificio_repo.find_all()

    def obtener_facultades(self):
        return self.facultad_repo.find_all()



    # VALIDACIÓN
    def validar_edificio(self, edificio: Edificio):
        if not edificio.nombre or not edificio.nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if edificio.id_facultad is None:
            raise ValueError("Debe seleccionar una facultad")

        # Verificar que la facultad existe
        facultad = self.facultad_repo.find_by_id(edificio.id_facultad)
        if not facultad:
            raise ValueError("La facultad seleccionada no existe")




    # CRUD
    def crear_edificio(self, edificio: Edificio):
        self.validar_edificio(edificio)
        return self.edificio_repo.insert(edificio)



    def actualizar_edificio(self, edificio: Edificio):
        if not edificio.id:
            raise ValueError("El edificio no tiene ID")
        self.validar_edificio(edificio)
        return self.edificio_repo.update(edificio)
    

    def eliminar_edificio(self, id_edificio: int):
        return self.edificio_repo.delete(id_edificio)