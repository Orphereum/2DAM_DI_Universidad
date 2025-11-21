from PySide6.QtWidgets import QWidget
from app.view.Pagina1_ui import Ui_Pagina1

class Pagina1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Pagina1()
        self.ui.setupUi(self)
