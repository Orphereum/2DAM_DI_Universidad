from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView
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
        
        # Tabla subvenciones
        header = self.tabla_subvenciones.horizontalHeader()
        # Primera columna (nombre) que se expanda
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        # Segunda columna (importe) tamaño fijo o contenido
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # Evitamos que se corte el texto
        self.tabla_subvenciones.setWordWrap(True)
        
        # Tabla proyectos
        header = self.tabla_proyectos.horizontalHeader()
        # Columna 0 → ID (mínimo necesario)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Columna 1 → Nombre (más importante)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        # Columna 2 → Descripción (también grande pero menos prioritaria)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        
        
        # Seleccion en tablas
        # Tabla proyectos
        self.ui.tabla_proyectos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tabla_proyectos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_proyectos.setStyleSheet("""
                QTableWidget::item:selected {
                background-color: #3daee9;
                color: black;
            }
        """)      
        self.tabla_proyectos.itemSelectionChanged.connect(self.proyecto_seleccionado)
        
        # Tabla Subvenciones
        self.ui.tabla_subvenciones.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tabla_subvenciones.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_subvenciones.setStyleSheet("""
                QTableWidget::item:selected {
                background-color: #3daee9;
                color: black;
            }
        """)      
        
        # Inicialización de clases
        self.proyecto_service = proyecto_service
        self.grupoInv_service = grupoInv_service
        
        # Inicializando métodos
        #self.cargar_datos()
        self.cargar_lista_gruposInv()
        
        # FUNCIONES DE LA VENTANA
        self.ui.comboBox_gruposInv.currentIndexChanged.connect(self.filtrar_por_grupo)
        
        # -----------------------
        # BOTONES LÓGICA INTERACCIÓN
        # -----------------------
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        
        
    def limpiar_campos(self):
        nombre = self.ui.nombre_txt.text().strip()
        descripcion = self.ui.descripcion_txt.toPlainText().strip()
        
        if not nombre and not descripcion:
            QMessageBox.information(self, "Información", "Debe haber algo escrito en alguno de los campos para poder limpiarlos")
            return
        
        # Si no, lo vaciamos e informamos
        self.ui.nombre_txt.clear()
        self.ui.descripcion_txt.clear()
        self.id_proyecto = None
        QMessageBox.information(self, "Liempeza de campos", "Se han limpiado los campos")
        
        
    def generar_tabla(self, tabla, datos):  
        tabla.setRowCount(len(datos))
        for linea, registro in enumerate(datos):
            for columna, valor in enumerate(registro):
                 # Si es la tabla de subvenciones, y es la columna de importe la 1, le ponemos formato de euros en miles.
                if tabla == self.tabla_subvenciones and columna == 1:
                    valor = f"{valor:,.0f} €".replace(",", ".")

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
        
        # cargar subvenciones
        self.cargar_subvenciones_proyecto(self.id_proyecto)
    
    def cargar_subvenciones_proyecto(self, id_proyecto):
        datos = self.proyecto_service.obtener_subvenciones(id_proyecto)
        
        self.generar_tabla(self.tabla_subvenciones, datos)
        