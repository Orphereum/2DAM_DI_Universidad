from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox, QTableWidgetItem
from app.view.EdificioPage_ui import Ui_EdificioPage
from app.models.edificio import Edificio


class EdificioPage(QWidget):
    def __init__(self, edificio_service, parent=None):
        super().__init__(parent)
        self.service = edificio_service

        self.ui = Ui_EdificioPage()
        self.ui.setupUi(self)

        self._configurar_tabla()
        self._conectar_eventos()
        self._cargar_facultades()

    # -------------------------
    # CONFIGURACIÓN DE LA TABLA
    # -------------------------
    def _configurar_tabla(self):
        tabla = self.ui.tableEdificios

        tabla.setColumnCount(2)
        tabla.setHorizontalHeaderLabels([
            "Nombre", "Facultad"
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
    # CONEXIÓN DE EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btnAnadir.clicked.connect(self.anadir_edificio)
        self.ui.btnEditar.clicked.connect(self.editar_edificio)
        self.ui.btnEliminar.clicked.connect(self.eliminar_edificio)
        self.ui.btnRefrescar.clicked.connect(self.refrescar_tabla)

    # -------------------------
    # CARGAR FACULTADES
    # -------------------------
    def _cargar_facultades(self):
        """Carga las facultades disponibles en el ComboBox"""
        try:
            facultades = self.service.obtener_facultades()
            self.ui.cbFacultad.clear()
            
            for facultad in facultades:
                self.ui.cbFacultad.addItem(facultad.nombre, facultad.id_facultad)
                
        except Exception as e:
            print(f"Error al cargar las facultades: {e}" )
    # -------------------------
    # AÑADIR EDIFICIO
    # -------------------------
    def anadir_edificio(self):
        nombre = self.ui.leNombre.text().strip()
        
        if not nombre:
            QMessageBox.warning(self, "Advertencia", "El nombre es obligatorio")
            return
            
        if self.ui.cbFacultad.currentIndex() < 0:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una facultad")
            return

        try:
            id_facultad = self.ui.cbFacultad.currentData()
            
            edificio = Edificio(
                id=None,
                nombre=nombre,
                id_facultad=id_facultad
            )
            
            self.service.crear_edificio(edificio)
            self.refrescar_tabla()
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Edificio creado correctamente")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear edificio: {str(e)}")

    # -------------------------
    # EDITAR EDIFICIO
    # -------------------------
    def editar_edificio(self):
        fila = self.ui.tableEdificios.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Advertencia", "Selecciona un edificio para editar")
            return

        try:
            edificios = self.service.obtener_edificios()
            edificio = edificios[fila]

            nombre = self.ui.leNombre.text().strip()
            if not nombre:
                QMessageBox.warning(self, "Advertencia", "El nombre es obligatorio")
                return
                
            if self.ui.cbFacultad.currentIndex() < 0:
                QMessageBox.warning(self, "Advertencia", "Debe seleccionar una facultad")
                return

            id_facultad = self.ui.cbFacultad.currentData()
            
            edificio_actualizado = Edificio(
                id=edificio.id,
                nombre=nombre,
                id_facultad=id_facultad
            )

            self.service.actualizar_edificio(edificio_actualizado)
            self.refrescar_tabla()
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Edificio editado correctamente")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al editar edificio: {str(e)}")

    # -------------------------
    # ELIMINAR EDIFICIO
    # -------------------------
    def eliminar_edificio(self):
        fila = self.ui.tableEdificios.currentRow()
        if fila < 0:
            QMessageBox.warning(self, "Advertencia", "Selecciona un edificio para eliminar")
            return

        try:
            edificios = self.service.obtener_edificios()
            edificio = edificios[fila]

            confirm = QMessageBox.question(
                self,
                "Confirmar",
                f"¿Eliminar el edificio '{edificio.nombre}'?",
                QMessageBox.Yes | QMessageBox.No
            )

            if confirm == QMessageBox.Yes:
                self.service.eliminar_edificio(edificio.id)
                self.refrescar_tabla()
                self._limpiar_formulario()
                QMessageBox.information(self, "Éxito", "Edificio eliminado")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar edificio: {str(e)}")

    # -------------------------
    # REFRESCAR TABLA
    # -------------------------
    def refrescar_tabla(self):
        try:
            edificios = self.service.obtener_edificios()
            facultades_dict = {f.id_facultad: f.nombre for f in self.service.obtener_facultades()}
            
            tabla = self.ui.tableEdificios
            tabla.setRowCount(0)

            for edificio in edificios:
                self._añadir_a_tabla(edificio, facultades_dict)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al refrescar tabla: {str(e)}")

    # -------------------------
    # UTILIDADES DE TABLA
    # -------------------------
    def _añadir_a_tabla(self, edificio: Edificio, facultades_dict: dict):
        fila = self.ui.tableEdificios.rowCount()
        self.ui.tableEdificios.insertRow(fila)

        self.ui.tableEdificios.setItem(
            fila, 0, QTableWidgetItem(edificio.nombre)
        )
        
        nombre_facultad = facultades_dict.get(edificio.id_facultad, "Desconocida")
        self.ui.tableEdificios.setItem(
            fila, 1, QTableWidgetItem(nombre_facultad)
        )

    def _limpiar_formulario(self):
        """Limpia los campos del formulario"""
        self.ui.leNombre.clear()
        self.ui.cbFacultad.setCurrentIndex(0)