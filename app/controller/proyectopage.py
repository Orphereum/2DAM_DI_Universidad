from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from app.view.ProyectoPage_ui import Ui_Proyecto_page


class ProyectoPage(QWidget):
    def __init__(self, proyecto_service, grupoInv_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Proyecto_page()
        self.ui.setupUi(self)
        
        # ------------------
        # variables globales
        self.id_proyecto = None
        # ------------------
        
        self.tabla_proyectos = self.ui.tabla_proyectos
        self.tabla_subvenciones = self.ui.tabla_subvenciones
        
        # Seleccion en tablas
        self.ui.tabla_proyectos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tabla_proyectos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_proyectos.setStyleSheet("""
                QTableWidget::item:selected {
                background-color: #3daee9;
                color: black;
            }
        """)      
        self.tabla_proyectos.itemSelectionChanged.connect(self.proyecto_seleccionado)
        
        # Inicialización de clases
        self.proyecto_service = proyecto_service
        self.grupoInv_service = grupoInv_service
        
        # Inicializando métodos
        #self.cargar_datos()
        self.cargar_lista_gruposInv()
        
        # FUNCIONES DE LA VENTANA
        self.ui.comboBox_gruposInv.currentIndexChanged.connect(self.filtrar_por_grupo)
        
        
        
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
        
        # primera opcion
        self.ui.comboBox_gruposInv.addItem("Seleccionar grupo", None)
        
        # demás opciones
        for grupo in datos:
            desplegable_grupos.addItem(
                grupo["nombre"], # nombre que se verá
                grupo["id_grupo"] # el id oculto para posteriores acciones
            )
            
    def filtrar_por_grupo(self):
        id_grupo = self.ui.comboBox_gruposInv.currentData()
        
        if id_grupo is None:
            self.tabla_proyectos.setRowCount(0)
            return
        
        datos = self.proyecto_service.filtrar_por_grupo(id_grupo)
        self.generar_tabla(self.tabla_proyectos, datos)
        
    def proyecto_seleccionado(self):
        fila = self.tabla_proyectos.currentRow()
        
        # pos 0 = id
        self.id_proyecto = int(self.tabla_proyectos.item(fila, 0).text())
        print(f"ID PRYECTO {self.id_proyecto}")  
        # pos 1 = nombre
        self.nombre_proyecto = self.tabla_proyectos.item(fila, 1).text()      
        self.ui.nombre_txt.setText(self.nombre_proyecto)
        # pos 2 = descripcion
        self.descrip_proyecto = self.tabla_proyectos.item(fila, 2).text()      
        self.ui.descripcion_txt.setPlainText(self.descrip_proyecto)
        
    