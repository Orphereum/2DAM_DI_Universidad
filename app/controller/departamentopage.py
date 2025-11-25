from PySide6.QtWidgets import QWidget
from app.view.DepartamentoPage.ui import Ui_Departamento

class DepartamentoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Departamento()
        self.ui.setupUi(self)
