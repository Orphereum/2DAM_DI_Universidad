from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from view.GradoPage_ui import Ui_Form
from service.grado_service import GradoService
from models.grado import Grado


class GradoPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.service = GradoService()
        self.grado_seleccionado_id = None

        self._configurar_tabla()
        self._conectar_eventos()
        self._bloquear_formulario()

    # CONFIGURACIÓN INICIAL

    def _configurar_tabla(self):
        self.ui.tbl_grados.setColumnCount(7)
        self.ui.tbl_grados.setHorizontalHeaderLabels([
            "ID", "Nombre", "Código", "Duración", "Créditos", "Tipo", "Estado"
        ])
        self.ui.tbl_grados.setColumnHidden(0, True)
        self.ui.tbl_grados.setSelectionBehavior(self.ui.tbl_grados.SelectRows)
        self.ui.tbl_grados.setEditTriggers(self.ui.tbl_grados.NoEditTriggers)

    def _conectar_eventos(self):
        self.ui.btn_nuevo.clicked.connect(self.nuevo_grado)
        self.ui.btn_editar.clicked.connect(self.editar_grado)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_grado)
        self.ui.btn_refrescar.clicked.connect(self.refrescar)

        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

        self.ui.tbl_grados.itemSelectionChanged.connect(
            self._tabla_cambio_seleccion
        )

    # CARGA DE DATOS (PREPARADO)

    def cargar_grados(self, id_facultad):
        """
        Este método lo llamará el AppController
        cuando haya una facultad seleccionada.
        """
        self.ui.tbl_grados.setRowCount(0)

        grados = self.service.obtener_grados_por_facultad(id_facultad)

        for grado in grados:
            row = self.ui.tbl_grados.rowCount()
            self.ui.tbl_grados.insertRow(row)

            self.ui.tbl_grados.setItem(row, 0, QTableWidgetItem(str(grado.id_grado)))
            self.ui.tbl_grados.setItem(row, 1, QTableWidgetItem(grado.nombre))
            self.ui.tbl_grados.setItem(row, 2, QTableWidgetItem(grado.codigo))
            self.ui.tbl_grados.setItem(row, 3, QTableWidgetItem(str(grado.duracion_anios)))
            self.ui.tbl_grados.setItem(row, 4, QTableWidgetItem(str(grado.creditos_totales)))
            self.ui.tbl_grados.setItem(row, 5, QTableWidgetItem(grado.tipo or ""))
            self.ui.tbl_grados.setItem(
                row, 6,
                QTableWidgetItem("Activo" if grado.estado else "Inactivo")
            )

    # CRUD

    def nuevo_grado(self):
        self.grado_seleccionado_id = None
        self._limpiar_formulario()
        self._desbloquear_formulario()

    def editar_grado(self):
        if not self.grado_seleccionado_id:
            QMessageBox.warning(self, "Aviso", "Selecciona un grado primero")
            return

        self._desbloquear_formulario()

    def eliminar_grado(self):
        if not self.grado_seleccionado_id:
            QMessageBox.warning(self, "Aviso", "Selecciona un grado")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que quieres eliminar el grado?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            self.service.eliminar_grado(self.grado_seleccionado_id)
            self.refrescar()

    def guardar(self):
        try:
            grado = Grado(
                id_grado=self.grado_seleccionado_id,
                nombre=self.ui.txt_nombre.text(),
                codigo=self.ui.txt_codigo.text(),
                duracion_anios=self.ui.sp_duracion.value(),
                creditos_totales=self.ui.sp_creditos.value(),
                tipo=self.ui.cb_tipo.currentText(),
                estado=self.ui.chk_activo.isChecked(),
                id_facultad=self._get_facultad_actual()
            )

            if self.grado_seleccionado_id:
                self.service.actualizar_grado(grado)
            else:
                self.service.crear_grado(grado)

            self.refrescar()
            self._bloquear_formulario()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def cancelar(self):
        self._bloquear_formulario()
        self._limpiar_formulario()

    # UTILIDADES

    def refrescar(self):
        self._limpiar_formulario()
        self._bloquear_formulario()

        id_facultad = self._get_facultad_actual()
        if id_facultad:
            self.cargar_grados(id_facultad)

    def _tabla_cambio_seleccion(self):
        items = self.ui.tbl_grados.selectedItems()
        if not items:
            return

        self.grado_seleccionado_id = int(items[0].text())

        self.ui.txt_nombre.setText(items[1].text())
        self.ui.txt_codigo.setText(items[2].text())
        self.ui.sp_duracion.setValue(int(items[3].text()))
        self.ui.sp_creditos.setValue(int(items[4].text()))
        self.ui.cb_tipo.setCurrentText(items[5].text())
        self.ui.chk_activo.setChecked(items[6].text() == "Activo")

    def _get_facultad_actual(self):
        """
        Preparado para cuando Facultad esté lista.
        """
        data = self.ui.cb_facultad.currentData()
        return data

    def _limpiar_formulario(self):
        self.ui.txt_nombre.clear()
        self.ui.txt_codigo.clear()
        self.ui.sp_duracion.setValue(0)
        self.ui.sp_creditos.setValue(0)
        self.ui.cb_tipo.setCurrentIndex(0)
        self.ui.chk_activo.setChecked(False)

    def _bloquear_formulario(self):
        self.ui.grp_formulario.setEnabled(False)

    def _desbloquear_formulario(self):
        self.ui.grp_formulario.setEnabled(True)
