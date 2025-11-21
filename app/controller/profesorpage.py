from PySide6.QtWidgets import QWidget
from app.view.ProfesorPage_ui import Ui_ProfesorPage

class ProfesorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfesorPage()
        self.ui.setupUi(self)