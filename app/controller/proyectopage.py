from PySide6.QtWidgets import QWidget, QMessageBox
from app.view.ProyectoPage_ui import Ui_Proyecto_page

class ProyectoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Proyecto_page()
        self.ui.setupUi(self)
        