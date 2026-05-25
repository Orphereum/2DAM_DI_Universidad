# app/service/universidad_service.py

class UniversidadService:
    def __init__(self, universidad_repo):
        """
        Inyección de dependencias del repositorio de la base de datos.
        De esta manera se aísla la lógica de negocio de las consultas SQL.
        """
        self.universidad_repo = universidad_repo

    def obtener_todas(self):
        """Recupera la lista de todas las universidades registradas."""
        return self.universidad_repo.obtener_todas()

    def crear_universidad(self, nombre):
        """Crea una nueva entidad Universidad."""
        return self.universidad_repo.crear_universidad(nombre)

    def actualizar_universidad(self, id_universidad, nombre):
        """Actualiza el nombre de una universidad existente por su ID."""
        return self.universidad_repo.actualizar_universidad(id_universidad, nombre)

    def eliminar_universidad(self, id_universidad):
        """
        Elimina el registro de una universidad. 
        Si existen restricciones relacionales (claves foráneas), el repositorio
        o la propia BBDD lanzará la excepción que capturaremos en el controlador.
        """
        return self.universidad_repo.eliminar_universidad(id_universidad)