from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from app.view.ClasesPage_ui import Ui_Form
from app.controller.clasedialog import ClaseDialog

class ClasePage(QWidget):
    def __init__(self, service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.service = service

        # Configuración inicial de la tabla
        self.ui.tblClases.setEditTriggers(QAbstractItemView.NoEditTriggers) # No editable directo
        self.ui.tblClases.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar fila completa
        
        # Conexiones de botones
        self.ui.btnCrear.clicked.connect(self.abrir_crear)
        self.ui.btnEditar.clicked.connect(self.abrir_editar)
        self.ui.btnBorrar.clicked.connect(self.borrar_clase)
        self.ui.btnRefrescar.clicked.connect(self.cargar_datos)

        # Cargar datos al iniciar
        self.cargar_datos()

    def cargar_datos(self):
        """Pide las clases al servicio y rellena la tabla"""
        try:
            clases = self.service.obtener_clases()
            self.ui.tblClases.setRowCount(0) # Limpiar tabla

            for row_idx, clase in enumerate(clases):
                self.ui.tblClases.insertRow(row_idx)
                
                # Columnas: 0:ID, 1:Nombre, 2:Capacidad, 3:Edificio (ID o Nombre)
                self.ui.tblClases.setItem(row_idx, 0, QTableWidgetItem(str(clase.id_clase)))
                self.ui.tblClases.setItem(row_idx, 1, QTableWidgetItem(clase.nombre))
                self.ui.tblClases.setItem(row_idx, 2, QTableWidgetItem(str(clase.capacidad)))
                self.ui.tblClases.setItem(row_idx, 3, QTableWidgetItem(str(clase.id_edificio)))
                
        except Exception as e:
            print(f"Error cargando tabla: {e}")

    def abrir_crear(self):
        dialog = ClaseDialog(self.service, parent=self)
        if dialog.exec(): # Si el usuario guardó
            self.cargar_datos()

    def abrir_editar(self):
        selected_row = self.ui.tblClases.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Aviso", "Seleccione una clase para editar.")
            return

        # Obtenemos el ID de la fila seleccionada (columna 0)
        id_item = self.ui.tblClases.item(selected_row, 0)
        id_clase = int(id_item.text())

        # Buscamos el objeto completo en BD
        clase = self.service.obtener_por_id(id_clase)
        
        if clase:
            dialog = ClaseDialog(self.service, clase=clase, parent=self)
            if dialog.exec():
                self.cargar_datos()

    def borrar_clase(self):
        selected_row = self.ui.tblClases.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Aviso", "Seleccione una clase para borrar.")
            return

        id_item = self.ui.tblClases.item(selected_row, 0)
        nombre_item = self.ui.tblClases.item(selected_row, 1)
        id_clase = int(id_item.text())
        
        confirm = QMessageBox.question(
            self, "Confirmar", 
            f"¿Seguro que desea eliminar la clase '{nombre_item.text()}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                self.service.eliminar_clase(id_clase)
                self.cargar_datos()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar: {e}")