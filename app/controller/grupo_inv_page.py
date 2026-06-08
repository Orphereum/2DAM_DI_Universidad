from pydoc import doc, html, html

from PySide6.QtWidgets import (
    QFileDialog, QInputDialog, QWidget, QHeaderView, QAbstractItemView, QMessageBox, QTableWidgetItem
)

from app.view.GrupoInv_ui import Ui_GruposInvView
from app.models.grupoInv import GrupoInvestigacion  

import os
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import QMessageBox

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
        self.ui.btnExportarPdf.clicked.connect(self.exportar_pdf)


    # -------------------------
    # NUEVO GRUPO (SIN DIÁLOGO)
    # -------------------------
    def nuevo_grupo(self):
        nombre, ok = QInputDialog.getText(self, "Nuevo Grupo", "Nombre del grupo:")
        if not ok or not nombre.strip():
            return

        descripcion, ok = QInputDialog.getText(self, "Nuevo Grupo", "Descripción:")
        if not ok:
            return

        fecha, ok = QInputDialog.getText(self, "Nuevo Grupo", "Fecha de creación (YYYY-MM-DD):")
        if not ok:
            return

        try:
            self.service.crear_grupo({
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha_creacion": fecha
            })
            self.refrescar_tabla()
            self._mostrar_estado("Grupo creado correctamente", "success")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    # -------------------------
    # EDITAR GRUPO (SIN DIÁLOGO)
    # -------------------------
    def editar_grupo(self):
        fila = self.ui.tbl_grupos.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Aviso", "Selecciona un grupo para editar")
            return

        grupo = self._grupos_cache[fila]

        nuevo_nombre, ok = QInputDialog.getText(self, "Editar Grupo", "Nuevo nombre:", text=grupo.nombre)
        if not ok:
            return

        nueva_desc, ok = QInputDialog.getText(self, "Editar Grupo", "Nueva descripción:", text=grupo.descripcion)
        if not ok:
            return

        nueva_fecha, ok = QInputDialog.getText(self, "Editar Grupo", "Nueva fecha (YYYY-MM-DD):", text=str(grupo.fecha_creacion))
        if not ok:
            return

        try:
            self.service.actualizar_grupo({
                "id_grupo": grupo.id_grupo,
                "nombre": nuevo_nombre,
                "descripcion": nueva_desc,
                "fecha_creacion": nueva_fecha
            })
            self.refrescar_tabla()
            self._mostrar_estado("Grupo actualizado correctamente", "success")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
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
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))


    # -------------------------
    # REFRESCAR TABLA
    # -------------------------
    def refrescar_tabla(self):
        # Obtener datos y limpiar tabla
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
        
    def exportar_pdf(self):
        if not self._grupos_cache:
            QMessageBox.warning(self, "Aviso", "No hay datos para exportar")
            return

        # Crear carpeta reports si no existe
        carpeta_reports = os.path.join(os.getcwd(),"reports")
        os.makedirs(carpeta_reports, exist_ok=True)

        ruta_pdf = os.path.join(carpeta_reports, "grupos_investigacion.pdf")

        # Construcción del HTML
        html = """
        <h1 style='text-align:center;'>Grupos de Investigación</h1>
        <table border='1' cellspacing='0' cellpadding='4' width='100%'>
            <tr style='background-color:#e0e0e0;'>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Fecha de creación</th>
            </tr>
        """

        for g in self._grupos_cache:
            html += f"""
            <tr>
                <td>{g.nombre}</td>
                <td>{g.descripcion}</td>
                <td>{g.fecha_creacion}</td>
            </tr>
            """

        html += "</table>"

        # Crear documento PDF
        doc = QTextDocument()
        doc.setHtml(html)

        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta_pdf)

        # PySide6 usa print_() en vez de print()
        doc.print_(printer)

        self._mostrar_estado(f"PDF exportado en: {ruta_pdf}", "success")

