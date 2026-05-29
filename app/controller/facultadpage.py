from PySide6.QtWidgets import (
    QWidget,
    QHeaderView,
    QAbstractItemView,
    QMessageBox,
    QTableWidgetItem,
    QFileDialog,
)

from app.view.FacultadPage_ui import Ui_FacultadPage
from app.models.facultad import Facultad
from app.reports.facultad_report import generar_informe_facultades


class FacultadPage(QWidget):
    def __init__(self, facultad_service, parent=None):
        super().__init__(parent)
        self.service = facultad_service

        self.ui = Ui_FacultadPage()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._conectar_eventos()
        self._cargar_combos()
        self.refrescar_tabla()

    def _configurar_tabla(self):
        tabla = self.ui.tableFacultades

        tabla.setColumnCount(4)
        tabla.setHorizontalHeaderLabels(["Nombre", "Teléfono", "Email", "Universidad"])

        tabla.verticalHeader().setVisible(False)
        tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        header = tabla.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        tabla.verticalHeader().setDefaultSectionSize(26)
        tabla.setAlternatingRowColors(True)

    def _conectar_eventos(self):
        self.ui.btnGuardar.clicked.connect(self.guardar_facultad)
        self.ui.btnEditar.clicked.connect(self.editar_facultad)
        self.ui.btnEliminar.clicked.connect(self.eliminar_facultad)
        self.ui.btnRefrescar.clicked.connect(self.refrescar_tabla)
        self.ui.btnInforme.clicked.connect(self.generar_informe_pdf)

    def _cargar_combos(self):
        self._cargar_universidades()
        self._cargar_profesores()

    def _cargar_universidades(self):
        try:
            universidades = self.service.obtener_universidades()
            self.ui.cbUniversidad.clear()
            for univ in universidades:
                self.ui.cbUniversidad.addItem(univ[1], univ[0])
        except Exception as e:
            print(f"Error al cargar universidades: {e}")

    def _cargar_profesores(self):
        try:
            profesores = self.service.obtener_profesores()
            self.ui.cbProfesor.clear()
            self.ui.cbProfesor.addItem("(Sin decano)", None)
            for prof in profesores:
                self.ui.cbProfesor.addItem(prof.nombre, prof.id)
        except Exception as e:
            print(f"Error al cargar profesores: {e}")

    def guardar_facultad(self):
        nombre = self.ui.leNombre.text().strip()
        telefono = self.ui.leTelefono.text().strip()
        email = self.ui.leEmail.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Advertencia", "El nombre es obligatorio")
            return

        if self.ui.cbUniversidad.currentIndex() < 0:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una universidad")
            return

        id_universidad = self.ui.cbUniversidad.currentData()
        id_profesor = self.ui.cbProfesor.currentData()

        try:
            facultad = Facultad(
                id=None,
                id_universidad=id_universidad,
                id_profesor=id_profesor,
                nombre=nombre,
                telefono=telefono,
                email=email,
            )
            self.service.crear_facultad(facultad)
            self.refrescar_tabla()
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Facultad creada correctamente")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear facultad: {str(e)}")

    def editar_facultad(self):
        fila = self.ui.tableFacultades.currentRow()
        if fila < 0:
            QMessageBox.warning(
                self, "Advertencia", "Selecciona una facultad para editar"
            )
            return

        try:
            facultades = self.service.obtener_facultades()
            facultad = facultades[fila]

            nombre = self.ui.leNombre.text().strip()
            if not nombre:
                QMessageBox.warning(self, "Advertencia", "El nombre es obligatorio")
                return

            if self.ui.cbUniversidad.currentIndex() < 0:
                QMessageBox.warning(
                    self, "Advertencia", "Debe seleccionar una universidad"
                )
                return

            id_universidad = self.ui.cbUniversidad.currentData()
            id_profesor = self.ui.cbProfesor.currentData()

            facultad_actualizada = Facultad(
                id=facultad.id,
                id_universidad=id_universidad,
                id_profesor=id_profesor,
                nombre=nombre,
                telefono=self.ui.leTelefono.text().strip(),
                email=self.ui.leEmail.text().strip(),
            )
            self.service.actualizar_facultad(facultad.id, facultad_actualizada)
            self.refrescar_tabla()
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Facultad editada correctamente")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al editar facultad: {str(e)}")

    def eliminar_facultad(self):
        fila = self.ui.tableFacultades.currentRow()
        if fila < 0:
            QMessageBox.warning(
                self, "Advertencia", "Selecciona una facultad para eliminar"
            )
            return

        try:
            facultades = self.service.obtener_facultades()
            facultad = facultades[fila]

            confirm = QMessageBox.question(
                self,
                "Confirmar",
                f"¿Eliminar la facultad '{facultad.nombre}'?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if confirm == QMessageBox.Yes:
                self.service.eliminar_facultad(facultad.id)
                self.refrescar_tabla()
                self._limpiar_formulario()
                QMessageBox.information(self, "Éxito", "Facultad eliminada")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar facultad: {str(e)}")

    def refrescar_tabla(self):
        try:
            facultades = self.service.obtener_facultades()
            universidades_dict = {
                u[0]: u[1] for u in self.service.obtener_universidades()
            }

            tabla = self.ui.tableFacultades
            tabla.setRowCount(0)

            for facultad in facultades:
                self._anadir_a_tabla(facultad, universidades_dict)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al refrescar tabla: {str(e)}")

    def generar_informe_pdf(self):
        try:
            facultades = self.service.obtener_facultades()

            if not facultades:
                QMessageBox.warning(
                    self,
                    "Aviso",
                    "No hay facultades registradas para generar el informe",
                )
                return

            universidades_dict = {
                u[0]: u[1] for u in self.service.obtener_universidades()
            }

            ruta, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar informe PDF",
                "informe_facultades.pdf",
                "PDF Files (*.pdf)",
            )

            if not ruta:
                return

            generar_informe_facultades(facultades, universidades_dict, ruta)

            QMessageBox.information(
                self, "Informe Generado", f"PDF creado exitosamente:\n{ruta}"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generando PDF:\n{str(e)}")

    def _anadir_a_tabla(self, facultad: Facultad, universidades_dict: dict):
        fila = self.ui.tableFacultades.rowCount()
        self.ui.tableFacultades.insertRow(fila)

        self.ui.tableFacultades.setItem(fila, 0, QTableWidgetItem(facultad.nombre))
        self.ui.tableFacultades.setItem(
            fila, 1, QTableWidgetItem(facultad.telefono or "")
        )
        self.ui.tableFacultades.setItem(fila, 2, QTableWidgetItem(facultad.email or ""))

        nombre_universidad = universidades_dict.get(
            facultad.id_universidad, "Desconocida"
        )
        self.ui.tableFacultades.setItem(fila, 3, QTableWidgetItem(nombre_universidad))

    def _limpiar_formulario(self):
        self.ui.leNombre.clear()
        self.ui.leTelefono.clear()
        self.ui.leEmail.clear()
        if self.ui.cbUniversidad.count() > 0:
            self.ui.cbUniversidad.setCurrentIndex(0)
        if self.ui.cbProfesor.count() > 0:
            self.ui.cbProfesor.setCurrentIndex(0)
        self.ui.tableFacultades.clearSelection()
