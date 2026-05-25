from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView
)

from PySide6.QtCore import Qt

from app.view.GrupoDebate_ui import Ui_GrupoDebate_page

from app.repository.grupo_debate_repo import GrupoDebateRepository
from app.service.grupo_debate_service import GrupoDebateService


class GrupoDebatePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_GrupoDebate_page()
        self.ui.setupUi(self)

        # Repository + Service
        self.repo = GrupoDebateRepository()
        self.service = GrupoDebateService(self.repo)

        # Variable selección
        self.id_grupo = None

        # Configuración tabla
        self._configurar_tabla()

        # Signals
        self._configurar_signals()

        # Carga inicial
        self.cargar_tabla()

    # ---------------------------------
    # CONFIG
    # ---------------------------------

    def _configurar_signals(self):

        self.ui.btn_guardar.clicked.connect(
            self.crear_grupo
        )

        self.ui.btn_editar.clicked.connect(
            self.editar_grupo
        )

        self.ui.btn_eliminar.clicked.connect(
            self.eliminar_grupo
        )

        self.ui.btn_limpiar.clicked.connect(
            self.limpiar_campos
        )

        self.ui.tabla_grupos.itemSelectionChanged.connect(
            self.seleccionar_grupo
        )

    def _configurar_tabla(self):

        tabla = self.ui.tabla_grupos

        tabla.verticalHeader().setVisible(False)

        tabla.setShowGrid(False)

        tabla.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        tabla.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        tabla.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )

        header = tabla.horizontalHeader()

        header.setSectionsMovable(False)

        header.setSectionsClickable(False)

        header.setStretchLastSection(True)

        header.setSectionResizeMode(QHeaderView.Fixed)

        tabla.setColumnWidth(0, 50)
        tabla.setColumnWidth(1, 180)
        tabla.setColumnWidth(2, 180)
        tabla.setColumnWidth(3, 250)
        tabla.setColumnWidth(4, 120)
        tabla.setColumnWidth(5, 100)

    # ---------------------------------
    # CRUD
    # ---------------------------------

    def crear_grupo(self):

        nombre = self.ui.inputNombre.text().strip()

        tema_principal = self.ui.inputTemaPrincipal.text().strip()

        descripcion = self.ui.inputDescripcion.text().strip()

        fecha_inicio = self.ui.inputFechaInicio.text().strip()

        estado = self.ui.inputEstado.text().strip()

        if not nombre:
            QMessageBox.warning(
                self,
                "Error",
                "El nombre es obligatorio"
            )
            return

        self.service.crear_grupo(
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado
        )

        QMessageBox.information(
            self,
            "OK",
            "Grupo creado correctamente"
        )

        self.cargar_tabla()

        self.limpiar_campos()

    def editar_grupo(self):

        if self.id_grupo is None:

            QMessageBox.information(
                self,
                "Info",
                "Selecciona un grupo"
            )

            return

        nombre = self.ui.inputNombre.text().strip()

        tema_principal = self.ui.inputTemaPrincipal.text().strip()

        descripcion = self.ui.inputDescripcion.text().strip()

        fecha_inicio = self.ui.inputFechaInicio.text().strip()

        estado = self.ui.inputEstado.text().strip()

        self.service.actualizar_grupo(
            self.id_grupo,
            nombre,
            tema_principal,
            descripcion,
            fecha_inicio,
            estado
        )

        QMessageBox.information(
            self,
            "OK",
            "Grupo actualizado correctamente"
        )

        self.cargar_tabla()

        self.limpiar_campos()

    def eliminar_grupo(self):

        if self.id_grupo is None:

            QMessageBox.information(
                self,
                "Info",
                "Selecciona un grupo"
            )

            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que quieres eliminar este grupo?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta != QMessageBox.Yes:
            return

        self.service.eliminar_grupo(
            self.id_grupo
        )

        QMessageBox.information(
            self,
            "OK",
            "Grupo eliminado correctamente"
        )

        self.cargar_tabla()

        self.limpiar_campos()

    # ---------------------------------
    # TABLA
    # ---------------------------------

    def cargar_tabla(self):

        datos = self.service.obtener_todos()

        tabla = self.ui.tabla_grupos

        tabla.setRowCount(len(datos))

        for fila, registro in enumerate(datos):

            for col, valor in enumerate(registro):

                item = QTableWidgetItem(str(valor))

                item.setTextAlignment(Qt.AlignCenter)

                tabla.setItem(
                    fila,
                    col,
                    item
                )

    def seleccionar_grupo(self):

        fila = self.ui.tabla_grupos.currentRow()

        if fila == -1:
            return

        self.id_grupo = int(
            self.ui.tabla_grupos.item(fila, 0).text()
        )

        self.ui.inputNombre.setText(
            self.ui.tabla_grupos.item(fila, 1).text()
        )

        self.ui.inputTemaPrincipal.setText(
            self.ui.tabla_grupos.item(fila, 2).text()
        )

        self.ui.inputDescripcion.setText(
            self.ui.tabla_grupos.item(fila, 3).text()
        )

        self.ui.inputFechaInicio.setText(
            self.ui.tabla_grupos.item(fila, 4).text()
        )

        self.ui.inputEstado.setText(
            self.ui.tabla_grupos.item(fila, 5).text()
        )

    # ---------------------------------
    # LIMPIAR
    # ---------------------------------

    def limpiar_campos(self):

        self.id_grupo = None

        self.ui.inputNombre.clear()

        self.ui.inputTemaPrincipal.clear()

        self.ui.inputDescripcion.clear()

        self.ui.inputFechaInicio.clear()

        self.ui.inputEstado.clear()

        self.ui.tabla_grupos.clearSelection()