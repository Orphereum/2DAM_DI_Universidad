from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QMessageBox,
    QHeaderView, QSizePolicy, QFileDialog
)

from app.view.ProfesorPage_ui import Ui_ProfesorPage
from app.models.profesor import Profesor
from app.repository.profesor_repo import ProfesorRepository
from app.service.profesor_service import ProfesorService
from app.reports.profesor_report import generar_pdf_profesores
from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QMessageBox,
    QHeaderView, QSizePolicy, QFileDialog,
    QPushButton, QDialog, QVBoxLayout, QFormLayout,
    QLineEdit, QComboBox, QCheckBox, QDialogButtonBox
)
from PySide6.QtWidgets import QSizePolicy


class ProfesorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfesorPage()
        self.ui.setupUi(self)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.profesor_repo = ProfesorRepository()
        self.service = ProfesorService(self.profesor_repo)

        self._selected_profesor_id: int | None = None
        #self._asignaturas_temporales = {}

        self._crear_botones_extra()
        self._configurar_tabla()
        self._configurar_signals()
        self._cargar_profesores()


    def _configurar_signals(self):
        self.ui.btbGuardar.clicked.connect(self.on_guardar)
        self.ui.btnActualizar.clicked.connect(self.on_editar)
        self.ui.btnEliminar.clicked.connect(self.on_eliminar)
        self.ui.btnLimpiar.clicked.connect(self.on_limpiar)
        self.ui.pushButton.clicked.connect(self.on_generar_pdf_profesores)
        self.ui.btnRefrescar.clicked.connect(self.on_refrescar)
        self.ui.btnNuevo.clicked.connect(self.on_nuevo_popup)
        self.ui.btnBusqueda.clicked.connect(self.on_buscar)
        self.ui.lnBusqueda.returnPressed.connect(self.on_buscar)
        self.ui.lnBusqueda.textChanged.connect(self._mostrar_boton_limpiar_busqueda)

        self.ui.tblProfesores.itemSelectionChanged.connect(self.on_tabla_seleccion)

        self.ui.txtNombre.returnPressed.connect(self.ui.txtCorreo.setFocus)
        self.ui.txtCorreo.returnPressed.connect(self.ui.txtTlf.setFocus)
        self.ui.txtTlf.returnPressed.connect(self.ui.txtTitulo.setFocus)
        self.ui.txtTitulo.returnPressed.connect(self.ui.cbDpto.setFocus)


    def _configurar_tabla(self):
        tbl = self.ui.tblProfesores
        tbl.setColumnCount(8)
        tbl.setHorizontalHeaderLabels([
            "ID", "Nombre", "Correo", "Teléfono", "Título",
            "Departamento", "Jefe", "Asignatura"
        ])

        tbl.setEditTriggers(tbl.EditTrigger.NoEditTriggers)
        tbl.setSelectionBehavior(tbl.SelectionBehavior.SelectRows)
        tbl.setSelectionMode(tbl.SelectionMode.SingleSelection)

        header = tbl.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        tbl.setColumnHidden(0, True)

        self.ui.tblProfesores.setStyleSheet("""
            QTableWidget {
                color: white;
                gridline-color: #444;
            }
        """)

    def on_buscar(self):
        texto = self.ui.lnBusqueda.text().strip().lower()

        if not texto:
            self._cargar_profesores()
            return

        profesores = self.service.obtener_profesores_con_asignaturas()
        filtrados = []

        for p in profesores:
            asignaturas = " ".join(p.asignaturas).lower() if p.asignaturas else ""

            if (
                texto in (p.nombre or "").lower()
                or texto in (p.correo or "").lower()
                or texto in (p.telefono or "").lower()
                or texto in (p.titulo or "").lower()
                or texto in asignaturas
            ):
                filtrados.append(p)

        self._pintar_profesores_en_tabla(filtrados)


    def on_limpiar_busqueda(self):
        self.ui.lnBusqueda.clear()
        self._cargar_profesores()


    def _mostrar_boton_limpiar_busqueda(self):
        self.btnLimpiarBusqueda.setVisible(bool(self.ui.lnBusqueda.text().strip()))

    def on_refrescar(self):
        self._cargar_profesores()
        QMessageBox.information(self, "Refrescado", "Lista de profesores actualizada.")

    def on_guardar(self):
        try:
            profesor = self._leer_formulario()
            asignatura = self.ui.lnAsignatura.text().strip()

            if self._selected_profesor_id is None:
                profesor = self.service.crear_profesor(profesor)
                mensaje = "Profesor creado correctamente"
            else:
                profesor.id = self._selected_profesor_id
                profesor = self.service.actualizar_profesor(profesor)
                mensaje = "Profesor actualizado correctamente"

            self.service.asignar_asignatura_por_nombre(profesor.id, asignatura)

            QMessageBox.information(self, "OK", mensaje)

            self._cargar_profesores()
            self._limpiar_formulario()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_editar(self):
        if self._selected_profesor_id is None:
            QMessageBox.information(self, "Editar", "Selecciona un profesor en la tabla primero.")
            return

        self.ui.txtNombre.setFocus()

    def on_eliminar(self):
        if self._selected_profesor_id is None:
            QMessageBox.information(self, "Eliminar", "Selecciona un profesor en la tabla primero.")
            return

        resp = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Seguro que quieres eliminar este profesor?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resp != QMessageBox.Yes:
            return

        try:
            self.service.eliminar_profesor(self._selected_profesor_id)
            #self._asignaturas_temporales.pop(self._selected_profesor_id, None)

            QMessageBox.information(self, "OK", "Profesor eliminado correctamente")

            self._cargar_profesores()
            self._limpiar_formulario()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_limpiar(self):
        self._limpiar_formulario()

    def _pintar_profesores_en_tabla(self, profesores):
        tabla = self.ui.tblProfesores
        tabla.setRowCount(len(profesores))

        for fila, p in enumerate(profesores):
            tabla.setItem(fila, 0, QTableWidgetItem(str(p.id or "")))
            tabla.setItem(fila, 1, QTableWidgetItem(p.nombre or ""))
            tabla.setItem(fila, 2, QTableWidgetItem(p.correo or ""))
            tabla.setItem(fila, 3, QTableWidgetItem(p.telefono or ""))
            tabla.setItem(fila, 4, QTableWidgetItem(p.titulo or ""))
            tabla.setItem(fila, 5, QTableWidgetItem(str(p.id_departamento or "")))
            tabla.setItem(fila, 6, QTableWidgetItem("Sí" if p.jefe_dtp else "No"))

            asignaturas = ", ".join(p.asignaturas) if p.asignaturas else "Sin asignaturas"
            tabla.setItem(fila, 7, QTableWidgetItem(asignaturas))

        tabla.resizeColumnsToContents()

    def on_tabla_seleccion(self):
        tbl = self.ui.tblProfesores
        items = tbl.selectedItems()

        if not items:
            return

        fila = items[0].row()
        id_item = tbl.item(fila, 0)

        if not id_item:
            return

        self._selected_profesor_id = int(id_item.text())

        self.ui.txtNombre.setText(tbl.item(fila, 1).text() if tbl.item(fila, 1) else "")
        self.ui.txtCorreo.setText(tbl.item(fila, 2).text() if tbl.item(fila, 2) else "")
        self.ui.txtTlf.setText(tbl.item(fila, 3).text() if tbl.item(fila, 3) else "")
        self.ui.txtTitulo.setText(tbl.item(fila, 4).text() if tbl.item(fila, 4) else "")

        dep_text = tbl.item(fila, 5).text() if tbl.item(fila, 5) else "1"
        dep_id = int(dep_text) if dep_text.isdigit() else 1
        self._set_departamento_combo(dep_id)

        jefe_text = tbl.item(fila, 6).text() if tbl.item(fila, 6) else "No"
        self.ui.checkJefe.setChecked(jefe_text.strip().lower() in ("sí", "si", "true", "1"))

        asignatura_text = tbl.item(fila, 7).text() if tbl.item(fila, 7) else ""
        self.ui.lnAsignatura.setText("" if asignatura_text == "Sin asignaturas" else asignatura_text)

    def _cargar_profesores(self):
        profesores = self.service.obtener_profesores_con_asignaturas()
        self._pintar_profesores_en_tabla(profesores)
        tabla = self.ui.tblProfesores
        tabla.setRowCount(len(profesores))

        for fila, p in enumerate(profesores):
            tabla.setItem(fila, 0, QTableWidgetItem(str(p.id or "")))
            tabla.setItem(fila, 1, QTableWidgetItem(p.nombre or ""))
            tabla.setItem(fila, 2, QTableWidgetItem(p.correo or ""))
            tabla.setItem(fila, 3, QTableWidgetItem(p.telefono or ""))
            tabla.setItem(fila, 4, QTableWidgetItem(p.titulo or ""))
            tabla.setItem(fila, 5, QTableWidgetItem(str(p.id_departamento or "")))
            tabla.setItem(fila, 6, QTableWidgetItem("Sí" if p.jefe_dtp else "No"))

            #asignatura_temporal = self._asignaturas_temporales.get(p.id)
                
            asignaturas = ", ".join(p.asignaturas) if p.asignaturas else "Sin asignaturas"
            tabla.setItem(fila, 7, QTableWidgetItem(asignaturas))

            tabla.setItem(fila, 7, QTableWidgetItem(asignaturas))

        tabla.resizeColumnsToContents()

    def _leer_formulario(self) -> Profesor:
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        telefono = self.ui.txtTlf.text().strip()
        titulo = self.ui.txtTitulo.text().strip()
        jefe = self.ui.checkJefe.isChecked()
        asignatura = self.ui.lnAsignatura.text().strip()

        id_departamento = self._get_departamento_id_from_combo()

        return Profesor(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            titulo=titulo,
            id_departamento=id_departamento,
            jefe_dtp=jefe,
            asignaturas=[asignatura] if asignatura else []
        )

    def _limpiar_formulario(self):
        self._selected_profesor_id = None

        self.ui.txtNombre.clear()
        self.ui.txtCorreo.clear()
        self.ui.txtTlf.clear()
        self.ui.txtTitulo.clear()
        self.ui.lnAsignatura.clear()
        self.ui.checkJefe.setChecked(False)

        if self.ui.cbDpto.count() > 0:
            self.ui.cbDpto.setCurrentIndex(0)

        self.ui.tblProfesores.clearSelection()
        self.ui.txtNombre.setFocus()

    def _get_departamento_id_from_combo(self) -> int:
        idx = self.ui.cbDpto.currentIndex()
        return 1 if idx <= 0 else 2

    def _set_departamento_combo(self, dep_id: int):
        if dep_id == 2 and self.ui.cbDpto.count() > 1:
            self.ui.cbDpto.setCurrentIndex(1)
        else:
            self.ui.cbDpto.setCurrentIndex(0)

    def on_generar_pdf_profesores(self):
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar informe de profesores",
            "informe_profesores.pdf",
            "PDF Files (*.pdf)"
        )

        if not ruta:
            return

        if not ruta.lower().endswith(".pdf"):
            ruta += ".pdf"

        try:
            profesores = self.service.obtener_profesores_con_asignaturas()

            for profesor in profesores:
                asignatura_temporal = self._asignaturas_temporales.get(profesor.id)
                if asignatura_temporal:
                    profesor.asignaturas = [asignatura_temporal]

            generar_pdf_profesores(profesores, ruta)

            QMessageBox.information(
                self,
                "OK",
                f"Informe guardado en:\n{ruta}"
            )

        except Exception as e:
            QMessageBox.warning(self, "Error al generar PDF", str(e))

    def _crear_botones_extra(self):

        self.btnLimpiarBusqueda = QPushButton("✕")
        self.btnLimpiarBusqueda.setFixedSize(35, 42)
        self.btnLimpiarBusqueda.setStyleSheet("color:white; font-size:18px; font-weight:bold;")
        self.btnLimpiarBusqueda.hide()

        self.ui.searchLayout.addWidget(self.btnLimpiarBusqueda)
        self.btnLimpiarBusqueda.clicked.connect(self.on_limpiar_busqueda)


    def on_nuevo_popup(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Nuevo profesor")
        dialog.setMinimumWidth(420)

        layout = QVBoxLayout(dialog)
        form = QFormLayout()

        txtNombre = QLineEdit()
        txtCorreo = QLineEdit()
        txtTelefono = QLineEdit()
        txtTitulo = QLineEdit()
        cbDpto = QComboBox()
        cbDpto.addItems(["Ciencias", "Ingenieria"])
        checkJefe = QCheckBox("Es jefe de departamento")
        txtAsignatura = QLineEdit()

        form.addRow("Nombre:", txtNombre)
        form.addRow("Correo:", txtCorreo)
        form.addRow("Teléfono:", txtTelefono)
        form.addRow("Título:", txtTitulo)
        form.addRow("Departamento:", cbDpto)
        form.addRow("Jefe:", checkJefe)
        form.addRow("Asignatura:", txtAsignatura)

        layout.addLayout(form)

        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(botones)

        botones.accepted.connect(dialog.accept)
        botones.rejected.connect(dialog.reject)

        if dialog.exec() != QDialog.Accepted:
            return

        profesor = Profesor(
            nombre=txtNombre.text().strip(),
            correo=txtCorreo.text().strip(),
            telefono=txtTelefono.text().strip(),
            titulo=txtTitulo.text().strip(),
            id_departamento=1 if cbDpto.currentIndex() == 0 else 2,
            jefe_dtp=checkJefe.isChecked(),
            asignaturas=[txtAsignatura.text().strip()] if txtAsignatura.text().strip() else []
        )

        try:
            profesor = self.service.crear_profesor(profesor)

            asignatura = txtAsignatura.text().strip()
            if asignatura:
                self.service.asignar_asignatura_por_nombre(profesor.id, asignatura)

            QMessageBox.information(self, "OK", "Profesor creado correctamente")
            self._cargar_profesores()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))