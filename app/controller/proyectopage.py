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
        self.nuevo_id = None
        # ------------------
        
        # ------------------
        # etiquetas de información
        # SOLO GUARDAR 1 proyecto seleccionado con sus subvenciones y su grupo de investigación
        self.ui.btn_generarPDF_proyecto.setToolTip("Se genera un informe del proyecto seleccionado junto con las subvenciones asociadas")
        self.ui.btn_generarPDF_proyecto.setToolTipDuration(5000)
        # GUARDAR todos los proyectos diferenciándolos de sus GRUPOS DE INVESTIGACIÓN.
        self.ui.btn_generarPDF_todos.setToolTip("Se genera un informe de todos los proyectos diferenciándolos de sus Grupos de Investigación")
        self.ui.btn_generarPDF_todos.setToolTipDuration(5000)
        # Tabla de proyectos vacía
        # EN MÉTODO DE EVENTO
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
        # Boton editar
        self.ui.btn_editar.clicked.connect(self.editar_proyecto)
        # Boton guardar
        self.ui.btn_guardar.clicked.connect(self.crear_proyecto)
        # Boton eliminar
        self.ui.btn_eliminar.clicked.connect(self.eliminar_proyecto)
        # Boton limpiar
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        
    # Método de evento al pasar el ratón por la tabla_proyecto vacía o cuando tenga registros
    def enterEvent(self, event):
        if self.tabla_proyectos.rowCount() == 0:
            self.tabla_proyectos.setToolTip("Para ver los proyectos en la tabla debes seleccionar algún grupo de Investigación \no crear algún proyecto en dicho grupo")
        else:
            self.tabla_proyectos.setToolTip("")

        super().enterEvent(event)
        
    def crear_proyecto(self):
        # primero comprobar que hay algunu grupoInv seleccionado en el comobox sino, muestrar un mensjae
        id_grupo = self.ui.comboBox_gruposInv.currentData()
        
        if id_grupo is None:
            QMessageBox.information(self, "Información", "Se necesita tener seleccionado algún grupo de investigación relacionado con el proyecto a crear")
            return 
        
        # se comprueba que los dos campos estén rellenados
        nombre = self.ui.nombre_txt.text().strip()
        descripcion = self.ui.descripcion_txt.toPlainText().strip()
        
        if not nombre or not descripcion:
            QMessageBox.warning(self, "Atención", "Todos los campos no pueden estar vacíos")
            return
        
        # insertar proyecto
        # guardar relacion N:M entre proyecto - grupoInv que esté seleccionado
        self.nuevo_id = self.proyecto_service.crear_proyecto(nombre, descripcion, id_grupo)
        # actualizar tabla y limpiar campos
        self.actualizar_tabla_proyectos()
        
        # seleccionar nuevo proyecto que se ha creado
        self.seleccionar_proyecto_por_id(self.nuevo_id)
        
        self.limpiar_campos()
    
    def editar_proyecto(self):
        if not hasattr(self, "id_proyecto") or self.id_proyecto is None:
            QMessageBox.information(self, "Información", "Debes selccionar un proyecto para poder editarlo")
            return
        
        nombre_nuevo = self.ui.nombre_txt.text().strip()
        descripcion_nueva = self.ui.descripcion_txt.toPlainText().strip()
        
        # si esta todo igual
        if (nombre_nuevo == self.nombre_proyecto and descripcion_nueva == self.descrip_proyecto):
            QMessageBox.information(self, "Sin cambios", "No se ha aplicado ningún cambio")
            return
        
        # si cambia algo de algún campos SÍ se actualiza
        self.proyecto_service.actualizar_proyecto(self.id_proyecto, nombre_nuevo, descripcion_nueva)
        
        # actualizar la tabla
        self.actualizar_tabla_proyectos()
        self.limpiar_campos()
        
        QMessageBox.information(self, "Cambios realizados", "Los cambios se han aplicado correctamente")
        
        # actualizar los valores originales
        self.nombre_proyecto = nombre_nuevo
        self.descrip_proyecto = descripcion_nueva
        
    def eliminar_proyecto(self):
        if not hasattr(self, "id_proyecto") or self.id_proyecto is None:
           QMessageBox.information(self, "Información", "Para elimnar algún proyecto primero tienes que seleccionarlo")
           return
       
        confirmacion = QMessageBox.question(self, "Confirmar eliminación", 
                                            "¿Estás seguro de querer borrar el proyecto seleccionado?", QMessageBox.Yes | QMessageBox.No)
        
        if confirmacion == QMessageBox.No:
            return
        
        # si es qie SI
        self.proyecto_service.eliminar_proyecto(self.id_proyecto)
        
        self.actualizar_tabla_proyectos()
        self.limpiar_campos()
        
        QMessageBox.information(self, "Proyecto eliminado", "El proyecto se ha eliminado correctamente")
     
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
        print("Campos limpios")
        
    def actualizar_tabla_proyectos(self):
        id_grupo = self.ui.comboBox_gruposInv.currentData()

        if id_grupo is None:
            self.tabla_proyectos.setRowCount(0)
            return
            
        datos = self.proyecto_service.obtener_por_grupo(id_grupo)

        self.generar_tabla(self.tabla_proyectos, datos)   
        
        
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
        
    # comprueba la tabla y busca el id nuevo que hemos recibido al crear un proyecto nuevo. 
    # Cuando coincida llama a proyecto_seleccionado para mostrarlo de manera más visual         
    def seleccionar_proyecto_por_id(self, id_proyecto):
        for fila in range(self.tabla_proyectos.rowCount()):
            item = self.tabla_proyectos.item(fila, 0)

            if item and int(item.text()) == id_proyecto:
                self.tabla_proyectos.selectRow(fila)
                self.proyecto_seleccionado()
                break
            
    def proyecto_seleccionado(self):
        fila = self.tabla_proyectos.currentRow()
        
        if fila == -1:
            return
        
        item_id = self.tabla_proyectos.item(fila,0)
        
        if item_id is None:
            return
    
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
        