from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QAbstractItemView,
    QMessageBox,
    QTableWidgetItem,
    QWidget,
)

from app.view.PublicacionPage_ui import Ui_Publicacion_page


class PublicacionPage(QWidget):
    def __init__(self, publicacion_service, parent=None):
        super().__init__(parent)
        self.ui = Ui_Publicacion_page()
        self.ui.setupUi(self)
        self.publicacion_service = publicacion_service
        self.id_publicacion = None

        self.tabla_publicaciones = self.ui.tabla_publicaciones
        self.tabla_publicaciones.verticalHeader().setVisible(False)
        self.tabla_publicaciones.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.tabla_publicaciones.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.tabla_publicaciones.itemSelectionChanged.connect(
            self.seleccionar_publicacion
        )
        self.ui.btn_guardar.clicked.connect(self.crear_publicacion)
        self.ui.btn_editar.clicked.connect(self.editar_publicacion)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_publicacion)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)

        self.cargar_grupos_debate()
        self.cargar_tabla()

    def cargar_grupos_debate(self):
        self.ui.comboGrupoDebate.clear()
        self.ui.comboGrupoDebate.addItem("Sin grupo de debate", None)

        for grupo in self.publicacion_service.obtener_grupos_debate():
            self.ui.comboGrupoDebate.addItem(
                grupo["nombre"] or f"Grupo {grupo['id_grupo']}",
                grupo["id_grupo"]
            )

    def crear_publicacion(self):
        datos = self._leer_formulario()

        try:
            self.publicacion_service.crear_publicacion(*datos)
        except ValueError as exc:
            QMessageBox.warning(self, "Error", str(exc))
            return

        self.cargar_tabla()
        self.limpiar_campos()
        QMessageBox.information(
            self,
            "Publicacion creada",
            "La publicacion se ha guardado correctamente"
        )

    def editar_publicacion(self):
        if self.id_publicacion is None:
            QMessageBox.information(
                self,
                "Informacion",
                "Selecciona una publicacion para editarla"
            )
            return

        datos = self._leer_formulario()

        try:
            self.publicacion_service.actualizar_publicacion(
                self.id_publicacion,
                *datos
            )
        except ValueError as exc:
            QMessageBox.warning(self, "Error", str(exc))
            return

        self.cargar_tabla()
        self.limpiar_campos()
        QMessageBox.information(
            self,
            "Publicacion actualizada",
            "Los cambios se han aplicado correctamente"
        )

    def eliminar_publicacion(self):
        if self.id_publicacion is None:
            QMessageBox.information(
                self,
                "Informacion",
                "Selecciona una publicacion para eliminarla"
            )
            return

        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminacion",
            "Seguro que quieres borrar la publicacion seleccionada?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.No:
            return

        try:
            self.publicacion_service.eliminar_publicacion(self.id_publicacion)
        except ValueError as exc:
            QMessageBox.warning(self, "Error", str(exc))
            return

        self.cargar_tabla()
        self.limpiar_campos()
        QMessageBox.information(
            self,
            "Publicacion eliminada",
            "La publicacion se ha eliminado correctamente"
        )

    def cargar_tabla(self):
        datos = self.publicacion_service.obtener_todos()
        self.tabla_publicaciones.setRowCount(len(datos))

        for fila, registro in enumerate(datos):
            valores = [
                registro["id_publicacion"],
                registro["titulo"],
                registro["descripcion"],
                registro["fecha_publicacion"],
                registro["tipo"],
                registro["id_grupoDebate"],
                registro["grupo_debate"],
            ]

            for columna, valor in enumerate(valores):
                texto = "" if valor is None else str(valor)
                self.tabla_publicaciones.setItem(
                    fila,
                    columna,
                    QTableWidgetItem(texto)
                )

    def seleccionar_publicacion(self):
        fila = self.tabla_publicaciones.currentRow()

        if fila == -1:
            return

        item_id = self.tabla_publicaciones.item(fila, 0)
        if item_id is None:
            return

        self.id_publicacion = int(item_id.text())
        self.ui.inputTitulo.setText(
            self._texto_tabla(fila, 1)
        )
        self.ui.inputDescripcion.setPlainText(
            self._texto_tabla(fila, 2)
        )

        fecha = QDate.fromString(self._texto_tabla(fila, 3), "yyyy-MM-dd")
        self.ui.inputFecha.setDate(
            fecha if fecha.isValid() else QDate.currentDate()
        )

        self.ui.inputTipo.setText(self._texto_tabla(fila, 4))

        id_grupo_texto = self._texto_tabla(fila, 5)
        id_grupo = int(id_grupo_texto) if id_grupo_texto else None
        index = self.ui.comboGrupoDebate.findData(id_grupo)
        self.ui.comboGrupoDebate.setCurrentIndex(index if index >= 0 else 0)

    def limpiar_campos(self):
        self.ui.inputTitulo.clear()
        self.ui.inputDescripcion.clear()
        self.ui.inputFecha.setDate(QDate.currentDate())
        self.ui.inputTipo.clear()
        self.ui.comboGrupoDebate.setCurrentIndex(0)
        self.tabla_publicaciones.clearSelection()
        self.id_publicacion = None

    def _leer_formulario(self):
        return (
            self.ui.inputTitulo.text().strip(),
            self.ui.inputDescripcion.toPlainText().strip(),
            self.ui.inputFecha.date().toString("yyyy-MM-dd"),
            self.ui.inputTipo.text().strip(),
            self.ui.comboGrupoDebate.currentData(),
        )

    def _texto_tabla(self, fila, columna):
        item = self.tabla_publicaciones.item(fila, columna)
        return item.text() if item else ""
