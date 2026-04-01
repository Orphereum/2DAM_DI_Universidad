from PySide6.QtWidgets import (
    QDialog, QTableWidgetItem,
    QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt

from app.view.InformeAsignaturasPage_ui import Ui_InformeAsignaturasPage
from app.reports.asignatura_report import generar_pdf_asignaturas
from PySide6.QtGui import QGuiApplication

class InformeAsignaturasPage(QDialog):

    def __init__(self, asignatura_service, parent=None):
        super().__init__(parent)

        self.service = asignatura_service

        self.ui = Ui_InformeAsignaturasPage()
        self.ui.setupUi(self)

        # 🔥 TAMAÑO PROFESIONAL
        self.setMinimumSize(1000, 700)
        self.resize(1100, 750)

        # 🔥 CENTRAR VENTANA
        self._centrar_ventana()

        # 🔥 CONTROL DE ESTADO
        self.informe_generado = False

        self._configurar_tabla()
        self._cargar_grados()
        self._cargar_tipos()
        self._conectar_eventos()

        # 🔒 DESACTIVAR EXPORTAR AL INICIO
        self.ui.btn_exportar.setEnabled(False)

    # -------------------------
    # CENTRAR VENTANA
    # -------------------------
  

    def _centrar_ventana(self):
     screen = QGuiApplication.primaryScreen().availableGeometry()

     x = (screen.width() - self.width()) // 2
     y = (screen.height() - self.height()) // 2

     self.move(x, y)

    # -------------------------
    # CONFIG TABLA
    # -------------------------
    def _configurar_tabla(self):
        self.ui.tbl_resultados.setColumnCount(5)
        self.ui.tbl_resultados.setHorizontalHeaderLabels([
            "Nombre", "Créditos", "Curso", "Cuatrimestre", "Obligatoria"
        ])

        # 🔥 TABLA MÁS PROFESIONAL
        self.ui.tbl_resultados.horizontalHeader().setStretchLastSection(True)
        self.ui.tbl_resultados.horizontalHeader().setDefaultSectionSize(150)

    # -------------------------
    # CARGAR GRADOS
    # -------------------------
    def _cargar_grados(self):
        for g in self.service.obtener_grados():
            self.ui.cb_grado.addItem(g.nombre, g.id_grado)

    # -------------------------
    # CARGAR TIPOS
    # -------------------------
    def _cargar_tipos(self):
        self.ui.cb_tipo.clear()
        self.ui.cb_tipo.addItem("Todas", None)
        self.ui.cb_tipo.addItem("Obligatorias", 1)
        self.ui.cb_tipo.addItem("Optativas", 0)

    # -------------------------
    # EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_generar.clicked.connect(self.generar_informe)
        self.ui.btn_exportar.clicked.connect(self.exportar_pdf)
        self.ui.btn_cerrar.clicked.connect(self.close)

        # 🔥 RESET AUTOMÁTICO AL CAMBIAR FILTROS
        self.ui.cb_grado.currentIndexChanged.connect(self._reset_estado)
        self.ui.cb_curso.currentIndexChanged.connect(self._reset_estado)
        self.ui.cb_cuatrimestre.currentIndexChanged.connect(self._reset_estado)
        self.ui.cb_tipo.currentIndexChanged.connect(self._reset_estado)

    # -------------------------
    # RESET ESTADO
    # -------------------------
    def _reset_estado(self):
        self.informe_generado = False
        self.ui.btn_exportar.setEnabled(False)

    # -------------------------
    # GENERAR INFORME
    # -------------------------
    def generar_informe(self):
        id_grado = self.ui.cb_grado.currentData()
        curso = self.ui.cb_curso.currentText()
        cuatri = self.ui.cb_cuatrimestre.currentText()
        tipo = self.ui.cb_tipo.currentData()

        if id_grado is None:
            QMessageBox.warning(self, "Error", "Selecciona un grado")
            return

        asignaturas = self.service.obtener_asignaturas_filtradas(
            id_grado, curso, cuatri, tipo
        )

        self.ui.tbl_resultados.setRowCount(0)

        for a in asignaturas:
            fila = self.ui.tbl_resultados.rowCount()
            self.ui.tbl_resultados.insertRow(fila)

            self.ui.tbl_resultados.setItem(fila, 0, QTableWidgetItem(a.nombre))
            self.ui.tbl_resultados.setItem(fila, 1, QTableWidgetItem(str(a.creditos)))
            self.ui.tbl_resultados.setItem(fila, 2, QTableWidgetItem(str(a.curso)))
            self.ui.tbl_resultados.setItem(fila, 3, QTableWidgetItem(str(a.cuatrimestre)))
            self.ui.tbl_resultados.setItem(
                fila, 4,
                QTableWidgetItem("Sí" if a.obligatoria else "No")
            )

        # 🔥 ACTIVAR EXPORTACIÓN
        self.informe_generado = True
        self.ui.btn_exportar.setEnabled(True)

        QMessageBox.information(self, "Informe", "Informe generado correctamente")

    # -------------------------
    # EXPORTAR PDF
    # -------------------------
    def exportar_pdf(self):

        if not self.informe_generado:
            QMessageBox.warning(
                self,
                "Acción no permitida",
                "Debes generar el informe antes de exportarlo."
            )
            return

        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar informe",
            "",
            "PDF (*.pdf)"
        )

        if not ruta:
            return

        id_grado = self.ui.cb_grado.currentData()
        curso = self.ui.cb_curso.currentText()
        cuatri = self.ui.cb_cuatrimestre.currentText()
        tipo = self.ui.cb_tipo.currentData()

        asignaturas = self.service.obtener_asignaturas_filtradas(
            id_grado, curso, cuatri, tipo
        )

        filtros = {
            "grado": self.ui.cb_grado.currentText(),
            "curso": curso,
            "cuatrimestre": cuatri,
            "tipo": self.ui.cb_tipo.currentText()
        }

        try:
            generar_pdf_asignaturas(asignaturas, ruta, filtros)
            QMessageBox.information(self, "Éxito", "PDF generado correctamente")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))