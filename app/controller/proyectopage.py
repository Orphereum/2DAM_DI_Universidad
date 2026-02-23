from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from app.view.ProyectoPage_ui import Ui_Proyecto_page


class ProyectoPage(QWidget):
    def __init__(self, proyecto_service, grupoInv_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Proyecto_page()
        self.ui.setupUi(self)
        
        self.tabla_proyectos = self.ui.tabla_proyectos
        self.tabla_subvenciones = self.ui.tabla_subvenciones
        # Inicialización de clases
        self.proyecto_service = proyecto_service
        self.grupoInv_service = grupoInv_service
        
        # Inicializando métodos
        self.cargar_datos()
        self.cargar_lista_gruposInv()
        
    def generar_tabla(self, tabla, datos):  
        tabla.setRowCount(len(datos))
        for linea, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                tabla.setItem(linea, columna, QTableWidgetItem(str(valor)))
        
    def cargar_datos(self):
        
        datos = self.proyecto_service.obtener_todos()
        
        self.generar_tabla(self.tabla_proyectos, datos)
        
    def cargar_lista_gruposInv(self):
        datos = self.grupoInv_service.cargar_lista_gruposInv()
        # datos devuelve objteos de grupo Investigacion --> id_grupo y nombre
        desplegable_grupos = self.ui.comboBox_gruposInv
        desplegable_grupos.clear()
        
        for grupo in datos:
            desplegable_grupos.addItem(
                grupo["nombre"], # nombre que se verá
                grupo["id_grupo"] # el id oculto para posteriores acciones
            )
            
