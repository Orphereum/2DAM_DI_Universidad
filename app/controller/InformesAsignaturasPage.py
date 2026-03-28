from PySide6.QtWidgets import QDialog, QTableWidgetItem,QMessageBox,QFileDialog
from app.view.InformeAsignaturasPage_ui import Ui_InformeAsignaturasPage
from app.reports.asignatura_report import generar_pdf_asignaturas

class InformeAsignaturasPage(QDialog):
    def __init__(self, asignatura_service, parent=None):
        super().__init__(parent)

        self.service = asignatura_service

        self.ui = Ui_InformeAsignaturasPage()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._cargar_grados()
        self._cargar_tipos()   # 🔥 IMPORTANTE
        self._conectar_eventos()
        self.ui.btn_exportar.clicked.connect(self.exportar_pdf)

    # -------------------------
    # CONFIG TABLA
    # -------------------------
    def _configurar_tabla(self):
        self.ui.tbl_resultados.setColumnCount(5)
        self.ui.tbl_resultados.setHorizontalHeaderLabels([
            "Nombre", "Créditos", "Curso", "Cuatrimestre", "Obligatoria"
        ])

    # -------------------------
    # CARGAR GRADOS
    # -------------------------
    def _cargar_grados(self):
        grados = self.service.obtener_grados()

        for grado in grados:
            self.ui.cb_grado.addItem(grado.nombre, grado.id_grado)

    # -------------------------
    # CARGAR TIPOS (🔥 CLAVE)
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
        self.ui.btn_cerrar.clicked.connect(self.close)

    # -------------------------
    # GENERAR INFORME
    # -------------------------
    def generar_informe(self):
        id_grado = self.ui.cb_grado.currentData()
        curso = self.ui.cb_curso.currentText()
        cuatrimestre = self.ui.cb_cuatrimestre.currentText()
        tipo = self.ui.cb_tipo.currentData()   # 🔥 IMPORTANTE

        if id_grado is None:
            return

        asignaturas = self.service.obtener_asignaturas_filtradas(
            id_grado, curso, cuatrimestre, tipo
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
    def exportar_pdf(self):
     ruta, _ = QFileDialog.getSaveFileName(
        self,
        "Guardar informe",
        "informe_asignaturas.pdf",
        "PDF Files (*.pdf)"
     )

     if not ruta:
        return

    # 🔥 filtros actuales
     id_grado = self.ui.cb_grado.currentData()
     curso = self.ui.cb_curso.currentText()
     cuatrimestre = self.ui.cb_cuatrimestre.currentText()
     tipo_texto = self.ui.cb_tipo.currentText()
     tipo = self.ui.cb_tipo.currentData()

     asignaturas = self.service.obtener_asignaturas_filtradas(
        id_grado, curso, cuatrimestre, tipo
     )

     filtros = {
        "grado": self.ui.cb_grado.currentText(),
        "curso": curso,
        "cuatrimestre": cuatrimestre,
        "tipo": tipo_texto
     }

     try:
        generar_pdf_asignaturas(asignaturas, ruta, filtros)
        QMessageBox.information(self, "Éxito", "PDF generado correctamente")
     except Exception as e:
        QMessageBox.critical(self, "Error", str(e))