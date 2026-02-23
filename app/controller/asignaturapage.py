from PySide6.QtWidgets import (
    QWidget, QHeaderView, QAbstractItemView, QMessageBox, QTableWidgetItem
)

from app.view.Asignatura_ui import Ui_AsignaturasView
from app.controller.asignaturadialog import AsignaturaDialog
from app.models.asignatura import Asignatura


class AsignaturaPage(QWidget):
    def __init__(self, asignatura_service, parent=None):
        super().__init__(parent)
        self.service = asignatura_service

        self.ui = Ui_AsignaturasView()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._conectar_eventos()

        # Lista en memoria (hasta tener repository)
   

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
    # CONEXIÓN DE EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_nueva.clicked.connect(self.nueva_asignatura)
        self.ui.btn_editar.clicked.connect(self.editar_asignatura)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_asignatura)
        self.ui.btn_refrescar.clicked.connect(self.refrescar_tabla)

    # -------------------------
    # NUEVA ASIGNATURA
    # -------------------------
    def nueva_asignatura(self):
     dialog = AsignaturaDialog(self.service, parent=self)

     if dialog.exec():
        try:
            self.service.crear_asignatura(dialog.resultado)
            self.refrescar_tabla()
            self.ui.lbl_estado.setText("Asignatura creada correctamente")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    # -------------------------
    # EDITAR ASIGNATURA
    # -------------------------
    def editar_asignatura(self):
     fila = self.ui.tbl_asignaturas.currentRow()
     if fila < 0:
        self.ui.lbl_estado.setText("Selecciona una asignatura para editar")
        return

     asignaturas = self.service.obtener_asignaturas()
     asignatura = asignaturas[fila]

     dialog = AsignaturaDialog(
        self.service,
        asignatura=asignatura,
        parent=self
     )

     if dialog.exec():
        try:
            self.service.actualizar_asignatura(dialog.resultado)
            self.refrescar_tabla()
            self.ui.lbl_estado.setText("Asignatura editada correctamente")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))


    # -------------------------
    # ELIMINAR ASIGNATURA
    # -------------------------
    def eliminar_asignatura(self):
     fila = self.ui.tbl_asignaturas.currentRow()
     if fila < 0:
        self.ui.lbl_estado.setText("Selecciona una asignatura para eliminar")
        return

     asignaturas = self.service.obtener_asignaturas()
     asignatura = asignaturas[fila]

     confirm = QMessageBox.question(
        self,
        "Confirmar",
        f"¿Eliminar la asignatura '{asignatura.nombre}'?",
        QMessageBox.Yes | QMessageBox.No
     )

     if confirm == QMessageBox.Yes:
        self.service.eliminar_asignatura(asignatura.id_asignatura)
        self.refrescar_tabla()
        self.ui.lbl_estado.setText("Asignatura eliminada")


    # -------------------------
    # REFRESCAR
    # -------------------------
    def refrescar_tabla(self):
     asignaturas = self.service.obtener_asignaturas()
     tabla = self.ui.tbl_asignaturas

     tabla.setRowCount(0)

     for asignatura in asignaturas:
        self._añadir_a_tabla(asignatura)

     self.ui.lbl_estado.setText("Tabla actualizada")

    # -------------------------
    # UTILIDADES DE TABLA
    # -------------------------
    def _añadir_a_tabla(self, asignatura: Asignatura):
        fila = self.ui.tbl_asignaturas.rowCount()
        self.ui.tbl_asignaturas.insertRow(fila)

        self.ui.tbl_asignaturas.setItem(
            fila, 0, QTableWidgetItem(asignatura.nombre)
        )
        self.ui.tbl_asignaturas.setItem(
            fila, 1, QTableWidgetItem(str(asignatura.creditos))
        )
        self.ui.tbl_asignaturas.setItem(
            fila, 2, QTableWidgetItem(str(asignatura.curso))
        )
        self.ui.tbl_asignaturas.setItem(
            fila, 3, QTableWidgetItem(str(asignatura.cuatrimestre))
        )
        self.ui.tbl_asignaturas.setItem(
            fila, 4,
            QTableWidgetItem("Sí" if asignatura.obligatoria else "No")
        )

    def _actualizar_fila(self, fila: int, asignatura: Asignatura):
        self.ui.tbl_asignaturas.item(fila, 0).setText(asignatura.nombre)
        self.ui.tbl_asignaturas.item(fila, 1).setText(str(asignatura.creditos))
        self.ui.tbl_asignaturas.item(fila, 2).setText(str(asignatura.curso))
        self.ui.tbl_asignaturas.item(fila, 3).setText(str(asignatura.cuatrimestre))
        self.ui.tbl_asignaturas.item(
            fila, 4
        ).setText("Sí" if asignatura.obligatoria else "No")
