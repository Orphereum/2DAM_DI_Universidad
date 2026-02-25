from service.facultad_service import FacultadService
from models.facultad import Facultad
from view.Facultad_ui import Ui_Dialog as FacultadUI
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox


class FacultadController:
    def __init__(self):
        self.ui = FacultadUI()
        self.ui.setupUi(self)
        self.facultad_service = FacultadService()

        self.ui.eliminarPorNombrePB.clicked.connect(self.eliminar_facultad)
        self.ui.actualizarPB.clicked.connect(self.actualizar_facultad)
        self.ui.guardarPB.clicked.connect(self.crear_facultad)
        self.ui.eliminarPB.clicked.connect(self.eliminar_facultad)

    def cargar_facultades_tabla(self):
        data = self.facultad_service.obtener_facultades()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Nombre", "Telefono", "Direccion"])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 200)

        for row_idx, facultad in enumerate(data):
            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(facultad.id_facultad)))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(facultad.nombre))
