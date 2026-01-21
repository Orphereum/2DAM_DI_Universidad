from app.models.clase import Clase

class ClaseService:
    def __init__(self, clase_repo, edificio_repo):
        self.clase_repo = clase_repo
        self.edificio_repo = edificio_repo

    def obtener_clases(self):
        return self.clase_repo.find_all()

    def obtener_edificios(self):
        # Necesario para llenar el ComboBox en el formulario
        return self.edificio_repo.find_all() 

    def guardar_clase(self, clase: Clase):
        self._validar(clase)
        if clase.id_clase:
            return self.clase_repo.update(clase)
        else:
            return self.clase_repo.insert(clase)

    def eliminar_clase(self, id_clase):
        return self.clase_repo.delete(id_clase)

    def _validar(self, clase: Clase):
        if not clase.nombre or len(clase.nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")
        if clase.capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        if not clase.id_edificio:
            raise ValueError("Debe asignar un edificio")