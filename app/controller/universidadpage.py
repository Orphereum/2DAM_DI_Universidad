import sys
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QFileDialog
from PySide6.QtCore import Qt

# Importación de la interfaz compilada
from app.view.UniversidadPage_ui import Ui_UniversidadPage

class UniversidadPage(QWidget):
    def __init__(self, parent=None, universidad_service=None):
        # Inicializamos la clase base QWidget de forma limpia
        if isinstance(parent, QWidget):
            super().__init__(parent)
        else:
            super().__init__()
            
        self.ui = Ui_UniversidadPage()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)

        # Variables globales internas de tracking
        self.id_universidad = None
        self.nombre_universidad = ""
        
        # Inyección o fallback automático del servicio
        if universidad_service is not None:
            self.universidad_service = universidad_service
        else:
            try:
                from app.service.universidad_service import UniversidadService
                self.universidad_service = UniversidadService(universidad_repo=None)
            except Exception:
                self.universidad_service = None
        
        # ------------------
        # Configuración de Tablas (Rutas de Enums corregidas sin marcas amarillas)
        # ------------------
        self.tabla_universidades = self.ui.tablaUniversidades
        self.tabla_universidades.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabla_universidades.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_universidades.horizontalHeader().setStretchLastSection(True)
        
        # Estilo de selección de fila adaptado al estándar del repositorio
        self.tabla_universidades.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #3daee9;
                color: black;
            }
        """)
        
        # Evento de cambio de selección en la tabla
        self.tabla_universidades.itemSelectionChanged.connect(self.universidad_seleccionada)
        
        # -----------------------
        # Conexión de Botones / Lógica de Interacción
        # -----------------------
        self.ui.btnCrear.clicked.connect(self.crear_universidad)
        self.ui.btnEditar.clicked.connect(self.preparar_edicion)
        self.ui.btnGuardar.clicked.connect(self.guardar_cambios)
        self.ui.btnEliminar.clicked.connect(self.eliminar_universidad)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        
        # Conexión del botón de reportes para el PDF de Jaime
        self.ui.btnReporte.clicked.connect(self.exportar_pdf)
        
        # Establecer el estado visual inicial del formulario
        self.establecer_estado_inicial_botones()
        
        # Carga controlada de información de la BD
        if self.universidad_service and getattr(self.universidad_service, 'universidad_repo', None) is not None:
            self.actualizar_tabla_universidades()
        else:
            print("[Aviso Jaime] Capa de datos simulada. Servicio o Repositorio no conectado todavía.")

    def establecer_estado_inicial_botones(self):
        """Define qué botones están activos por defecto al entrar al formulario."""
        self.ui.btnCrear.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnGuardar.setEnabled(False)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.inputNombre.setEnabled(True)

    def actualizar_tabla_universidades(self):
        """Obtiene todas las universidades del servicio y rellena la tabla."""
        datos = self.universidad_service.obtener_todas()
        
        self.tabla_universidades.setRowCount(len(datos))
        for fila, registro in enumerate(datos):
            item_id = QTableWidgetItem(str(registro[0]))
            item_id.setTextAlignment(Qt.AlignCenter)
            
            self.tabla_universidades.setItem(fila, 0, item_id)
            self.tabla_universidades.setItem(fila, 1, QTableWidgetItem(str(registro[1])))

    def universidad_seleccionada(self):
        """Maneja el evento cuando el usuario hace clic sobre una fila de la tabla."""
        fila = self.tabla_universidades.currentRow()
        if fila == -1:
            return
            
        item_id = self.tabla_universidades.item(fila, 0)
        if item_id is None:
            return
            
        self.id_universidad = int(item_id.text())
        self.nombre_universidad = self.tabla_universidades.item(fila, 1).text()
        
        self.ui.inputNombre.setText(self.nombre_universidad)
        
        self.ui.btnCrear.setEnabled(False)
        self.ui.btnEditar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnGuardar.setEnabled(False)

    def crear_universidad(self):
        """Toma el texto introducido e inserta una nueva Universidad."""
        nombre = self.ui.inputNombre.text().strip()
        
        if not nombre:
            QMessageBox.warning(self, "Atención", "El campo nombre no puede estar vacío")
            return
            
        self.universidad_service.crear_universidad(nombre)
        
        self.actualizar_tabla_universidades()
        self.limpiar_campos_internos()
        self.establecer_estado_inicial_botones()
        
        QMessageBox.information(self, "Éxito", f"Universidad '{nombre}' creada correctamente")

    def preparar_edicion(self):
        """Habilita el botón Guardar cuando se pulsa 'Editar'."""
        if self.id_universidad is None:
            QMessageBox.information(self, "Información", "Debes seleccionar una universidad para poder editarla")
            return
            
        self.ui.btnGuardar.setEnabled(True)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.inputNombre.setFocus()

    def guardar_cambios(self):
        """Aplica las modificaciones del registro editado."""
        nombre_nuevo = self.ui.inputNombre.text().strip()
        
        if not nombre_nuevo:
            QMessageBox.warning(self, "Atención", "El nombre no puede quedar vacío")
            return
            
        if nombre_nuevo == self.nombre_universidad:
            QMessageBox.information(self, "Sin cambios", "No se ha aplicado ningún cambio")
            self.establecer_estado_inicial_botones()
            self.limpiar_campos_internos()
            return
            
        self.universidad_service.actualizar_universidad(self.id_universidad, nombre_nuevo)
        
        self.actualizar_tabla_universidades()
        self.limpiar_campos_internos()
        self.establecer_estado_inicial_botones()
        
        QMessageBox.information(self, "Cambios realizados", "Los cambios se han aplicado correctamente")

    def eliminar_universidad(self):
        """Elimina la universidad controlando las restricciones relacionales en el servicio."""
        if self.id_universidad is None:
            QMessageBox.information(self, "Información", "Para eliminar una universidad primero tienes que seleccionarla")
            return
            
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de querer borrar la universidad '{self.nombre_universidad}'?", 
            QMessageBox.Yes | QMessageBox.No
        )
        
        if confirmacion == QMessageBox.No:
            return
            
        try:
            self.universidad_service.eliminar_universidad(self.id_universidad)
            self.actualizar_tabla_universidades()
            self.limpiar_campos_internos()
            self.establecer_estado_inicial_botones()
            QMessageBox.information(self, "Universidad eliminada", "La universidad se ha eliminado correctamente")
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Error de Restricción Relacional", 
                f"No se puede eliminar la universidad debido a dependencias activas en el sistema.\n{str(e)}"
            )

    def exportar_pdf(self):
        """Abre un cuadro de diálogo nativo del sistema para exportar el informe en PDF."""
        try:
            # Intentamos llamar al método estructurado del servicio
            datos_universidades = self.universidad_service.obtener_todo_para_reporte()
        except AttributeError:
            # Fallback seguro en caso de que la capa de repositorios de la BBDD falte por completar
            QMessageBox.warning(
                self, 
                "Servicio en desarrollo", 
                "El backend para el reporte estructurado aún se está acoplando.\nGenerando reporte simplificado con los datos actuales de la tabla..."
            )
            # Reconstruimos una estructura compatible rápida leyendo los datos de la tabla visual
            datos_universidades = []
            filas = self.tabla_universidades.rowCount()
            for f in range(filas):
                nom_u = self.tabla_universidades.item(f, 1).text()
                datos_universidades.append({"nombre": nom_u, "facultades": []})

        if not datos_universidades:
            QMessageBox.information(self, "Sin datos", "No hay registros disponibles para exportar.")
            return

        # 📂 DEFINE LA RUTA POR DEFECTO EN APP/REPORTS
        # Usamos os.path.join para evitar problemas con las barras según el sistema operativo
        import os
        ruta_defecto = os.path.join("reports", "Informe_Universidades.pdf")

        # Lanzamiento del asistente de guardado de ficheros del S.O.
        ruta_guardado, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Informe de Universidades - Jaime Ponce",
            ruta_defecto,  # <-- 🛠️ Aquí le pasamos la ruta para que abra directamente en app/reports
            "Archivos PDF (*.pdf)"
        )

        if not ruta_guardado:
            return

        # Importación selectiva y llamada al generador de Jaime Ponce
        try:
            from app.reports.universidad_report import GeneradorInformeUniversidades_Facultades
            
            generador = GeneradorInformeUniversidades_Facultades(datos_universidades)
            generador.generar(ruta_guardado)
            
            QMessageBox.information(self, "Éxito", "¡El informe en PDF se ha generado correctamente!")
        except Exception as e:
            QMessageBox.critical(self, "Error de Exportación", f"No se pudo estructurar el documento PDF:\n{str(e)}")
        """Abre un cuadro de diálogo nativo del sistema para exportar el informe en PDF."""
        try:
            # Intentamos llamar al método estructurado del servicio
            datos_universidades = self.universidad_service.obtener_todo_para_reporte()
        except AttributeError:
            # Fallback seguro en caso de que la capa de repositorios de la BBDD falte por completar
            QMessageBox.warning(
                self, 
                "Servicio en desarrollo", 
                "El backend para el reporte estructurado aún se está acoplando.\nGenerando reporte simplificado con los datos actuales de la tabla..."
            )
            # Reconstruimos una estructura compatible rápida leyendo los datos de la tabla visual
            datos_universidades = []
            filas = self.tabla_universidades.rowCount()
            for f in range(filas):
                nom_u = self.tabla_universidades.item(f, 1).text()
                datos_universidades.append({"nombre": nom_u, "facultades": []})

        if not datos_universidades:
            QMessageBox.information(self, "Sin datos", "No hay registros disponibles para exportar.")
            return

        # Lanzamiento del asistente de guardado de ficheros del S.O.
        ruta_guardado, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Informe de Universidades - Jaime Ponce",
            "Informe_Universidades.pdf",
            "Archivos PDF (*.pdf)"
        )

        if not ruta_guardado:
            return

        # Importación selectiva y llamada al generador de Jaime Ponce
        try:
            from app.reports.universidad_report import GeneradorInformeUniversidades_Facultades
            
            generador = GeneradorInformeUniversidades_Facultades(datos_universidades)
            generador.generar(ruta_guardado)
            
            QMessageBox.information(self, "Éxito", "¡El informe en PDF se ha generado correctamente!")
        except Exception as e:
            QMessageBox.critical(self, "Error de Exportación", f"No se pudo estructurar el documento PDF:\n{str(e)}")

    def limpiar_campos(self):
        """Acción vinculada al botón 'Limpiar' de la UI."""
        nombre_actual = self.ui.inputNombre.text().strip()
        if not nombre_actual and self.id_universidad is None:
            QMessageBox.information(self, "Información", "El formulario ya se encuentra limpio")
            return
            
        self.limpiar_campos_internos()
        self.establecer_estado_inicial_botones()

    def limpiar_campos_internos(self):
        """Limpia los widgets de entrada y las variables de tracking."""
        self.tabla_universidades.clearSelection()
        self.ui.inputNombre.clear()
        self.id_universidad = None
        self.nombre_universidad = ""