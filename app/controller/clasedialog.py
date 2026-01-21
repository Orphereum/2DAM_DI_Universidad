from PySide6.QtWidgets import QDialog, QMessageBox
from app.view.ClaseDialog_ui import Ui_Dialog  # Asegúrate de que Ui_Dialog coincida con el nombre en tu archivo _ui.py
from app.models.clase import Clase

class ClaseDialog(QDialog):
    def __init__(self, service, clase=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.service = service
        self.clase = clase # Si es None, estamos creando. Si tiene datos, editando.

        self._cargar_edificios()
        
        if self.clase:
            self._cargar_datos_en_formulario()

        # Conectar botones del buttonBox (Save/Cancel)
        self.ui.buttonBox.accepted.connect(self.guardar)
        self.ui.buttonBox.rejected.connect(self.reject)

    def _cargar_edificios(self):
        """Llena el ComboBox con los edificios disponibles"""
        try:
            edificios = self.service.obtener_edificios()
            self.ui.cbEdificio.clear()
            for ed in edificios:
                # addItem(texto_visible, dato_oculto_ID)
                self.ui.cbEdificio.addItem(ed.nombre, ed.id_edificio)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar edificios: {e}")

    def _cargar_datos_en_formulario(self):
        """Rellena los campos si estamos editando"""
        self.ui.txtNombre.setText(self.clase.nombre)
        self.ui.spCapacidad.setValue(self.clase.capacidad)
        
        # Buscar el edificio de esta clase en el combo y seleccionarlo
        index = self.ui.cbEdificio.findData(self.clase.id_edificio)
        if index >= 0:
            self.ui.cbEdificio.setCurrentIndex(index)

    def guardar(self):
        """Recoge datos, valida y guarda"""
        nombre = self.ui.txtNombre.text().strip()
        capacidad = self.ui.spCapacidad.value()
        id_edificio = self.ui.cbEdificio.currentData()

        if not nombre:
            QMessageBox.warning(self, "Aviso", "El nombre no puede estar vacío.")
            return

        if id_edificio is None:
            QMessageBox.warning(self, "Aviso", "Debe seleccionar un edificio.")
            return

        # Crear objeto modelo
        nueva_clase = Clase(
            id_clase=self.clase.id_clase if self.clase else None,
            nombre=nombre,
            capacidad=capacidad,
            id_edificio=id_edificio
        )

        try:
            self.service.guardar_clase(nueva_clase)
            self.accept() # Cierra la ventana devolviendo True
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar: {e}")