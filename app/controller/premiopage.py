from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt
from app.view.PremioEx_ui import Ui_PremioPage
from app.service.premio_service import PremioService
from app.controller.premiodialog import PremioDialog

class PremioPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PremioPage()
        self.ui.setupUi(self)
        
        # Inicializamos el servicio
        self.service = PremioService()
        
        # Configurar tabla
        self.ui.tablePremios.setColumnWidth(0, 50)  # ID estrecho
        self.ui.tablePremios.setColumnWidth(1, 200) # Nombre ancho
        self.ui.tablePremios.horizontalHeader().setStretchLastSection(True)
        
        # Conectar botones
        self.ui.btnNuevo.clicked.connect(self.nuevo_premio)
        self.ui.btnEditar.clicked.connect(self.editar_premio)
        self.ui.btnEliminar.clicked.connect(self.eliminar_premio)
        
        # Cargar datos al iniciar
        self.cargar_premios()

    def cargar_premios(self):
        """Limpia la tabla y recarga los datos desde la BD"""
        premios = self.service.obtener_premios()
        self.ui.tablePremios.setRowCount(0)
        
        for row, premio in enumerate(premios):
            self.ui.tablePremios.insertRow(row)
            # Columna 0: ID
            item_id = QTableWidgetItem(str(premio.id_premio))
            item_id.setFlags(item_id.flags() ^ Qt.ItemIsEditable) # Solo lectura
            self.ui.tablePremios.setItem(row, 0, item_id)
            
            # Columna 1: Nombre
            self.ui.tablePremios.setItem(row, 1, QTableWidgetItem(premio.nombre_premio))
            
            # Columna 2: Descripción
            self.ui.tablePremios.setItem(row, 2, QTableWidgetItem(premio.descripcion_premio))

    def nuevo_premio(self):
        dialog = PremioDialog(self)
        if dialog.exec():
            nuevo_premio = dialog.get_data()
            if nuevo_premio:
                try:
                    self.service.crear_premio(nuevo_premio)
                    self.cargar_premios()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")

    def editar_premio(self):
        seleccion = self.ui.tablePremios.selectedItems()
        if not seleccion:
            QMessageBox.warning(self, "Aviso", "Selecciona un premio para editar")
            return
            
        # Obtenemos el ID de la fila seleccionada (columna 0)
        row = seleccion[0].row()
        id_premio = int(self.ui.tablePremios.item(row, 0).text())
        nombre = self.ui.tablePremios.item(row, 1).text()
        descripcion = self.ui.tablePremios.item(row, 2).text()
        
        # Creamos objeto temporal para pasar al dialogo
        from app.models.premio_excelencia import PremioExcelencia
        premio_actual = PremioExcelencia(id_premio, nombre, descripcion)
        
        dialog = PremioDialog(self, premio_actual)
        if dialog.exec():
            premio_editado = dialog.get_data()
            if premio_editado:
                try:
                    self.service.actualizar_premio(premio_editado)
                    self.cargar_premios()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error al actualizar: {e}")

    def eliminar_premio(self):
        seleccion = self.ui.tablePremios.selectedItems()
        if not seleccion:
            QMessageBox.warning(self, "Aviso", "Selecciona un premio para eliminar")
            return
            
        row = seleccion[0].row()
        id_premio = int(self.ui.tablePremios.item(row, 0).text())
        
        confirmacion = QMessageBox.question(
            self, "Confirmar", 
            "¿Estás seguro de eliminar este premio?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if confirmacion == QMessageBox.Yes:
            try:
                self.service.borrar_premio(id_premio)
                self.cargar_premios()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar: {e}")