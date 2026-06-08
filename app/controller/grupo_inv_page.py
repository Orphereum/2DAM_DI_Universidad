from PySide6.QtWidgets import (
    QWidget, QHeaderView, QAbstractItemView, QMessageBox, QTableWidgetItem
)

from app.view.GrupoInv_ui import Ui_GruposInvView
from app.models.grupoInv import GrupoInvestigacion  

class GrupoInvPage(QWidget):
    def __init__(self, grupo_service, parent=None):
        super().__init__(parent)
        self.service = grupo_service

        # Cache de datos
        self._grupos_cache = []

        self.ui = Ui_GruposInvView()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._conectar_eventos()

        # Cargar datos iniciales
        self.refrescar_tabla()

    # -------------------------
    # CONFIGURACIÓN DE LA TABLA
    # -------------------------
    def _configurar_tabla(self):
        tabla = self.ui.tbl_grupos

        tabla.setColumnCount(3)
        tabla.setHorizontalHeaderLabels([
            "Nombre", "Descripción", "Fecha de creación"
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
    # EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_nuevo.clicked.connect(self.nuevo_grupo)
        self.ui.btn_editar.clicked.connect(self.editar_grupo)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_grupo)
        self.ui.btn_refrescar.clicked.connect(self.refrescar_tabla)

        # Si más adelante tienes informes o gráficos:
        # self.ui.btnExportarPdf.clicked.connect(self.abrir_informes)
        # self.ui.btnGraficos.clicked.connect(self.abrir_graficos)

    # -------------------------
    # NUEVO GRUPO (SIN DIÁLOGO)
    # -------------------------
    def nuevo_grupo(self):
        QMessageBox.information(
            self,
            "Función no implementada",
            "No tienes diálogos, así que no puedo crear un grupo desde una ventana.\n"
            "Si quieres, puedo generarte una ventana simple para introducir datos."
        )

    # -------------------------
    # EDITAR GRUPO (SIN DIÁLOGO)
    # -------------------------
    def editar_grupo(self):
        fila = self.ui.tbl_grupos.currentRow()

        if fila < 0:
            QMessageBox.warning(self, "Aviso", "Selecciona un grupo para editar")
            return

        QMessageBox.information(
            self,
            "Función no implementada",
            "No tienes diálogos, así que no puedo editar un grupo desde una ventana.\n"
            "Si quieres, puedo generarte una ventana simple para editar datos."
        )

    # -------------------------
    # ELIMINAR GRUPO
    # -------------------------
    def eliminar_grupo(self):
        fila = self.ui.tbl_grupos.currentRow()

        if fila < 0:
            QMessageBox.warning(self, "Aviso", "Selecciona un grupo para eliminar")
            return

        grupo = self._grupos_cache[fila]

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Eliminar el grupo '{grupo.nombre}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                self.service.eliminar_grupo(grupo.id_grupo)
                self.refrescar_tabla()
                self._mostrar_estado("Grupo eliminado correctamente", "success")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    # -------------------------
    # REFRESCAR TABLA
    # -------------------------
    def refrescar_tabla(self):
        self._grupos_cache = self.service.obtener_grupos()

        tabla = self.ui.tbl_grupos
        tabla.setRowCount(0)

        for grupo in self._grupos_cache:
            self._añadir_a_tabla(grupo)

    # -------------------------
    # AÑADIR FILA A TABLA
    # -------------------------
    def _añadir_a_tabla(self, grupo: GrupoInvestigacion):
        fila = self.ui.tbl_grupos.rowCount()
        self.ui.tbl_grupos.insertRow(fila)

        self.ui.tbl_grupos.setItem(fila, 0, QTableWidgetItem(grupo.nombre))
        self.ui.tbl_grupos.setItem(fila, 1, QTableWidgetItem(grupo.descripcion))
        self.ui.tbl_grupos.setItem(fila, 2, QTableWidgetItem(str(grupo.fecha_creacion)))

    # -------------------------
    # MENSAJES DE ESTADO
    # -------------------------
    def _mostrar_estado(self, texto, tipo="info"):
        self.ui.lbl_estado.setText(texto)
        self.ui.lbl_estado.setProperty("estado", tipo)
        self.ui.lbl_estado.style().unpolish(self.ui.lbl_estado)
        self.ui.lbl_estado.style().polish(self.ui.lbl_estado)