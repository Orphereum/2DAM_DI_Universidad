from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from app.view.SubvencionPage_ui import Ui_Subvencion_page
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView


class SubvencionPage(QWidget):
    def __init__(self, subvencion_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Subvencion_page()
        self.ui.setupUi(self)
        self.subvencion_service = subvencion_service
        self.ui.tabla_subvenciones.verticalHeader().setVisible(False)
        self.ui.tabla_subvenciones.setShowGrid(False)
        self.ui.tabla_subvenciones.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded)

        header = self.ui.tabla_subvenciones.horizontalHeader()

        header.setSectionsMovable(False)
        header.setSectionsClickable(False)
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Fixed)

        self.ui.tabla_subvenciones.setColumnWidth(0, 50)
        self.ui.tabla_subvenciones.setColumnWidth(1, 200)
        self.ui.tabla_subvenciones.setColumnWidth(2, 100)
        self.ui.tabla_subvenciones.setColumnWidth(3, 100)
        self.ui.tabla_subvenciones.setColumnWidth(4, 120)
        self.ui.tabla_subvenciones.setColumnWidth(5, 120)
        self.ui.tabla_subvenciones.setColumnWidth(6, 80)

        # variables
        self.id_subvencion = None

        # configurar tabla
        self.ui.tabla_subvenciones.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        self.ui.tabla_subvenciones.setSelectionMode(
            QAbstractItemView.SingleSelection)
        self.ui.tabla_subvenciones.itemSelectionChanged.connect(
            self.seleccionar_subvencion)

        # botones
        self.ui.btn_guardar.clicked.connect(self.crear_subvencion)
        self.ui.btn_editar.clicked.connect(self.editar_subvencion)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_subvencion)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)

        # cargar datos
        self.cargar_tabla()

    # -------------------------
    # CRUD
    # -------------------------

    def crear_subvencion(self):
        nombre = self.ui.inputNombre.text().strip()
        importe_min = self.ui.inputImporteMin.text().strip()
        importe_max = self.ui.inputImporteMax.text().strip()
        fecha_inicio = self.ui.inputFechaInicio.text().strip()
        fecha_fin = self.ui.inputFechaFin.text().strip()
        estado = self.ui.inputEstado.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre es obligatorio")
            return

        self.subvencion_service.crear_subvencion(
            nombre, float(importe_min), float(importe_max),
            fecha_inicio, fecha_fin, estado
        )

        self.cargar_tabla()
        self.limpiar_campos()

    def editar_subvencion(self):
        if self.id_subvencion is None:
            QMessageBox.information(self, "Info", "Selecciona una subvención")
            return

        nombre = self.ui.inputNombre.text()
        importe_min = self.ui.inputImporteMin.text()
        importe_max = self.ui.inputImporteMax.text()
        fecha_inicio = self.ui.inputFechaInicio.text()
        fecha_fin = self.ui.inputFechaFin.text()
        estado = self.ui.inputEstado.text()

        self.subvencion_service.actualizar_subvencion(
            self.id_subvencion,
            nombre, float(importe_min), float(importe_max),
            fecha_inicio, fecha_fin, estado
        )

        self.cargar_tabla()
        self.limpiar_campos()

    def eliminar_subvencion(self):
        if self.id_subvencion is None:
            QMessageBox.information(self, "Info", "Selecciona una subvención")
            return

        self.subvencion_service.eliminar_subvencion(self.id_subvencion)

        self.cargar_tabla()
        self.limpiar_campos()

    # -------------------------
    # TABLA
    # -------------------------

    def cargar_tabla(self):
        datos = self.subvencion_service.obtener_todos()

        self.ui.tabla_subvenciones.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            for col, valor in enumerate(registro):
                self.ui.tabla_subvenciones.setItem(
                    fila, col, QTableWidgetItem(str(valor)))

    def seleccionar_subvencion(self):
        fila = self.ui.tabla_subvenciones.currentRow()

        if fila == -1:
            return

        self.id_subvencion = int(
            self.ui.tabla_subvenciones.item(fila, 0).text())

        self.ui.inputNombre.setText(
            self.ui.tabla_subvenciones.item(fila, 1).text())
        self.ui.inputImporteMin.setText(
            self.ui.tabla_subvenciones.item(fila, 2).text())
        self.ui.inputImporteMax.setText(
            self.ui.tabla_subvenciones.item(fila, 3).text())
        self.ui.inputFechaInicio.setText(
            self.ui.tabla_subvenciones.item(fila, 4).text())
        self.ui.inputFechaFin.setText(
            self.ui.tabla_subvenciones.item(fila, 5).text())
        self.ui.inputEstado.setText(
            self.ui.tabla_subvenciones.item(fila, 6).text())

    # -------------------------
    # LIMPIAR
    # -------------------------

    def limpiar_campos(self):
        self.ui.inputNombre.clear()
        self.ui.inputImporteMin.clear()
        self.ui.inputImporteMax.clear()
        self.ui.inputFechaInicio.clear()
        self.ui.inputFechaFin.clear()
        self.ui.inputEstado.clear()
        self.id_subvencion = None
