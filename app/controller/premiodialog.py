from PySide6.QtWidgets import QDialog, QMessageBox
from app.view.PremioDialog_ui import Ui_PremioDialog
from app.models.premio_excelencia import PremioExcelencia

class PremioDialog(QDialog):
    def __init__(self, parent=None, premio=None):
        super().__init__(parent)
        self.ui = Ui_PremioDialog()
        self.ui.setupUi(self)
        
        self.premio = premio
        
        # Si nos pasan un premio, es una edición: rellenamos los campos
        if self.premio:
            self.setWindowTitle("Editar Premio")
            self.ui.txtNombre.setText(self.premio.nombre_premio)
            self.ui.txtDescripcion.setPlainText(self.premio.descripcion_premio)
        else:
            self.setWindowTitle("Nuevo Premio")

    def get_data(self):
        """Devuelve un objeto PremioExcelencia con los datos del formulario"""
        nombre = self.ui.txtNombre.text().strip()
        descripcion = self.ui.txtDescripcion.toPlainText().strip()
        
        # Validacion simple
        if not nombre:
            QMessageBox.warning(self, "Aviso", "El nombre es obligatorio")
            return None
            
        # Mantenemos el ID si existe (edición) o None (nuevo)
        id_premio = self.premio.id_premio if self.premio else None
        
        return PremioExcelencia(id_premio, nombre, descripcion)