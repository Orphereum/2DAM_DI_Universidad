from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView

from app.view.Asignaturas_ui import Ui_AsignaturasView


class AsignaturaPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AsignaturasView()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._conectar_eventos()

    # -------------------------
    # CONFIGURACIÓN DE LA TABLA
    # -------------------------
    def _configurar_tabla(self):
     tabla = self.ui.tbl_asignaturas

     tabla.setColumnCount(5)
     tabla.setHorizontalHeaderLabels([
        "Nombre", "Créditos", "Curso", "Cuatrimestre", "Obligatoria"
     ])

     tabla.verticalHeader().setVisible(False)

     tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
     tabla.setSelectionMode(QAbstractItemView.SingleSelection)
     tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

     header = tabla.horizontalHeader()
     header.setSectionResizeMode(QHeaderView.Stretch)

     tabla.verticalHeader().setDefaultSectionSize(26)
     tabla.setAlternatingRowColors(True)


    # -------------------------
    # CONEXIÓN DE EVENTOS (placeholder)
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_nueva.clicked.connect(self.nueva_asignatura)
        self.ui.btn_editar.clicked.connect(self.editar_asignatura)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_asignatura)
        self.ui.btn_refrescar.clicked.connect(self.refrescar_tabla)

    # -------------------------
    # MÉTODOS CRUD (VACÍOS DE MOMENTO)
    # -------------------------
    def nueva_asignatura(self):
        self.ui.lbl_estado.setText("Nueva asignatura")

    def editar_asignatura(self):
        fila = self.ui.tbl_asignaturas.currentRow()
        if fila < 0:
            self.ui.lbl_estado.setText("Selecciona una asignatura para editar")
            return
        self.ui.lbl_estado.setText("Editar asignatura")

    def eliminar_asignatura(self):
        fila = self.ui.tbl_asignaturas.currentRow()
        if fila < 0:
            self.ui.lbl_estado.setText("Selecciona una asignatura para eliminar")
            return
        self.ui.lbl_estado.setText("Eliminar asignatura")

    def refrescar_tabla(self):
        self.ui.lbl_estado.setText("Tabla actualizada")
