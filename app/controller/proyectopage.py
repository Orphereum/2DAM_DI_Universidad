from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from app.view.ProyectoPage_ui import Ui_Proyecto_page
from app.repository.proyecto_repo import ProyectoRepository
from app.service.proyecto_service import ProyectoService

class ProyectoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Proyecto_page()
        self.ui.setupUi(self)
        
        self.tabla = self.ui.tabla_proyectos
        # Inicialización de clases
        self.proyecto_repo = ProyectoRepository()
        self.proyecto_service = ProyectoService(self.proyecto_repo)
        
        # Inicializando métodos
        self.cargar_datos()
        
    def generar_tabla(self, tabla, datos):  
        tabla.setRowCount(len(datos))
        for linea, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                tabla.setItem(linea, columna, QTableWidgetItem(str(valor)))
        
    def cargar_datos(self):
        
        datos = self.proyecto_service.obtener_todos()
        
        self.generar_tabla(self.tabla, datos)



