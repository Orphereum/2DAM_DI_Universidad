from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from app.view.ProfesorPage_ui import Ui_ProfesorPage
from app.models.profesor import Profesor
from app.repository.profesor_repo import ProfesorRepository
#<FALTA el de departamento 
from app.service.profesor_service import ProfesorService


class ProfesorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfesorPage()
        self.ui.setupUi(self)

        self.profesor_repo = ProfesorRepository()
        self.service = ProfesorService(self.profesor_repo)

        #llamamos las funciones
        self._configurar_tabla()

    
    #cargamos las columnas en la tabla
    def _configurar_tabla(self):
        tbl = self.ui.tblProfesores
        tbl.setColumnCount(7)
        tbl.setHorizontalHeaderLabels([
           "ID", "Nombre", "Correo", "Teléfono", "Título", "Departamento", "Jefe" 
        ])
        tbl.setEditTriggers(tbl.EditTrigger.NoEditTriggers)
        tbl.setSelectionBehavior(tbl.SelectionBehavior.SelectRows)
        tbl.setSelectionMode(tbl.SelectionMode.SingleSelection)

        header = tbl.horizontalHeader()
        header.setStretchLastSection(True)

