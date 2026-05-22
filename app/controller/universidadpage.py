from PySide6.QtWidgets import QWidget
from app.view.UniversidadPage_ui import Ui_UniversidadPage

class UniversidadPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UniversidadPage()
        self.ui.setupUi(self)
