from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QHeaderView
from PySide6.QtCore import Qt

from app.view.ProfesorPage_ui import Ui_ProfesorPage
from app.models.profesor import Profesor
from app.repository.profesor_repo import ProfesorRepository
from app.service.profesor_service import ProfesorService
from PySide6.QtWidgets import QSizePolicy


class ProfesorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfesorPage()
        self.ui.setupUi(self)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.profesor_repo = ProfesorRepository()
        self.service = ProfesorService(self.profesor_repo)

        # Estado: ID seleccionado (None = modo crear)
        self._selected_profesor_id: int | None = None

        self._configurar_tabla()
        self._configurar_signals()

        # Carga inicial
        self._cargar_profesores()

    # -------------------------
    # UI / SIGNALS
    # -------------------------
    def _configurar_signals(self):
        # CRUD
        self.ui.btbGuardar.clicked.connect(self.on_guardar)
        self.ui.btnActualizar.clicked.connect(self.on_editar)   # "Editar"
        self.ui.btnEliminar.clicked.connect(self.on_eliminar)
        self.ui.btnLimpiar.clicked.connect(self.on_limpiar)

        self.ui.tblProfesores.itemSelectionChanged.connect(self.on_tabla_seleccion)

        # Navegación con enter
        self.ui.txtNombre.returnPressed.connect(self.ui.txtCorreo.setFocus)
        self.ui.txtCorreo.returnPressed.connect(self.ui.txtTlf.setFocus)
        self.ui.txtTlf.returnPressed.connect(self.ui.txtTitulo.setFocus)
        self.ui.txtTitulo.returnPressed.connect(self.ui.cbDpto.setFocus)

    def _configurar_tabla(self):
        tbl = self.ui.tblProfesores
        tbl.setColumnCount(7)
        tbl.setHorizontalHeaderLabels([
            "ID", "Nombre", "Correo", "Teléfono", "Título", "Departamento", "Jefe"
        ])

        tbl.setEditTriggers(tbl.EditTrigger.NoEditTriggers)
        tbl.setSelectionBehavior(tbl.SelectionBehavior.SelectRows)
        tbl.setSelectionMode(tbl.SelectionMode.SingleSelection)

        header = tbl.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
       # header.setStretchLastSection(True)

        # ocultar la columna ID 
        tbl.setColumnHidden(0, True)


    # CRUD

    def on_guardar(self):
        """
        Si hay selección -> UPDATE
        Si no hay selección -> INSERT
        """
        try:
            profesor = self._leer_formulario()

            if self._selected_profesor_id is None:
                # CREATE
                self.service.crear_profesor(profesor)
                QMessageBox.information(self, "OK", "Profesor creado correctamente")
            else:
                # UPDATE
                profesor.id = self._selected_profesor_id
                self.service.actualizar_profesor(profesor)
                QMessageBox.information(self, "OK", "Profesor actualizado correctamente")

            self._cargar_profesores()
            self._limpiar_formulario()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_editar(self):
        """
        No hace el update (eso lo hace Guardar),
        solo obliga a que haya selección y te pone foco en el nombre.
        """
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
            QMessageBox.information(self, "OK", "Profesor eliminado correctamente")
            self._cargar_profesores()
            self._limpiar_formulario()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_limpiar(self):
        self._limpiar_formulario()

    # TABLa

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

        # Rellenar formulario
        self.ui.txtNombre.setText(tbl.item(fila, 1).text() if tbl.item(fila, 1) else "")
        self.ui.txtCorreo.setText(tbl.item(fila, 2).text() if tbl.item(fila, 2) else "")
        self.ui.txtTlf.setText(tbl.item(fila, 3).text() if tbl.item(fila, 3) else "")
        self.ui.txtTitulo.setText(tbl.item(fila, 4).text() if tbl.item(fila, 4) else "")

        dep_text = tbl.item(fila, 5).text() if tbl.item(fila, 5) else "1"
        dep_id = int(dep_text) if dep_text.isdigit() else 1
        self._set_departamento_combo(dep_id)

        jefe_text = tbl.item(fila, 6).text() if tbl.item(fila, 6) else "No"
        self.ui.checkJefe.setChecked(jefe_text.strip().lower() in ("sí", "si", "true", "1"))

    def _cargar_profesores(self):
        profesores = self.service.obtener_profesores()
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

        tabla.resizeColumnsToContents()

    def _leer_formulario(self) -> Profesor:
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        telefono = self.ui.txtTlf.text().strip()
        titulo = self.ui.txtTitulo.text().strip()
        jefe = self.ui.checkJefe.isChecked()

        # Mapeo temporal: combo -> id_departamento
        id_departamento = self._get_departamento_id_from_combo()

        return Profesor(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            titulo=titulo,
            id_departamento=id_departamento,
            jefe_dtp=jefe
        )

    def _limpiar_formulario(self):
        self._selected_profesor_id = None

        self.ui.txtNombre.clear()
        self.ui.txtCorreo.clear()
        self.ui.txtTlf.clear()
        self.ui.txtTitulo.clear()
        self.ui.checkJefe.setChecked(False)

        # reset combo
        if self.ui.cbDpto.count() > 0:
            self.ui.cbDpto.setCurrentIndex(0)

        # limpiar selección tabla
        self.ui.tblProfesores.clearSelection()
        self.ui.txtNombre.setFocus()

    # Departamento (temporal pq aun no hau)

    def _get_departamento_id_from_combo(self) -> int:
        """
        Sin repo de departamento:
        - index 0 => 1
        - index 1 => 2
        """
        idx = self.ui.cbDpto.currentIndex()
        return 1 if idx <= 0 else 2

    def _set_departamento_combo(self, dep_id: int):
        if dep_id == 2 and self.ui.cbDpto.count() > 1:
            self.ui.cbDpto.setCurrentIndex(1)
        else:
            self.ui.cbDpto.setCurrentIndex(0)