from PySide6.QtWidgets import QDialog, QMessageBox
from app.view.AsignaturaDialog_ui import Ui_AsignaturaDialog
from app.models.asignatura import Asignatura


class AsignaturaDialog(QDialog):
    """
    Diálogo para crear o editar una asignatura.
    NO guarda nada en BD.
    Devuelve una instancia de Asignatura si todo es válido.
    """

    def __init__(self, asignatura_service, asignatura=None, parent=None):
        super().__init__(parent)

        self.service = asignatura_service
        self.asignatura = asignatura  # None = nueva, != None = edición

        self.ui = Ui_AsignaturaDialog()
        self.ui.setupUi(self)

        # 👇 AQUÍ SE APLICA EL ESTILO
       

        self._configurar_dialogo()
        self._cargar_grados()
        self._cargar_datos_si_edicion()
        self._conectar_eventos()

    # -------------------------
    # ESTILO DEL DIÁLOGO
    # -------------------------
   

    # -------------------------
    # CONFIGURACIÓN INICIAL
    # -------------------------
    def _configurar_dialogo(self):
        if self.asignatura:
            self.setWindowTitle("Editar asignatura")
            self.ui.lblTitulo.setText("Editar asignatura")
        else:
            self.setWindowTitle("Nueva asignatura")
            self.ui.lblTitulo.setText("Nueva asignatura")

    # -------------------------
    # CARGA DE COMBOS
    # -------------------------
    def _cargar_grados(self):
        self.ui.cb_grado.clear()
        grados = self.service.obtener_grados()

        for grado in grados:
            self.ui.cb_grado.addItem(grado.nombre, grado.id_grado)

    # -------------------------
    # EDICIÓN
    # -------------------------
    def _cargar_datos_si_edicion(self):
        if not self.asignatura:
            return

        self.ui.txt_nombre.setText(self.asignatura.nombre)
        self.ui.sp_creditos.setValue(self.asignatura.creditos)
        self.ui.cb_curso.setCurrentText(str(self.asignatura.curso))
        self.ui.cb_cuatrimestre.setCurrentText(str(self.asignatura.cuatrimestre))
        self.ui.chk_obligatoria.setChecked(self.asignatura.obligatoria)

        index = self.ui.cb_grado.findData(self.asignatura.grado_fk)
        if index >= 0:
            self.ui.cb_grado.setCurrentIndex(index)

    # -------------------------
    # EVENTOS
    # -------------------------
    def _conectar_eventos(self):
        self.ui.btn_guardar.clicked.connect(self._guardar)
        self.ui.btn_cancelar.clicked.connect(self.reject)

    # -------------------------
    # GUARDAR / VALIDAR
    # -------------------------
    def _guardar(self):
        try:
            asignatura = self._crear_asignatura_desde_formulario()
            self.resultado = asignatura
            self.accept()
        except ValueError as e:
            QMessageBox.warning(self, "Datos incorrectos", str(e))

    # -------------------------
    # CREACIÓN DE MODELO
    # -------------------------
    def _crear_asignatura_desde_formulario(self) -> Asignatura:
        nombre = self.ui.txt_nombre.text().strip()
        creditos = self.ui.sp_creditos.value()
        curso = int(self.ui.cb_curso.currentText())
        cuatrimestre = int(self.ui.cb_cuatrimestre.currentText())
        grado_fk = self.ui.cb_grado.currentData()
        obligatoria = self.ui.chk_obligatoria.isChecked()

        asignatura = Asignatura(
            id_asignatura=self.asignatura.id_asignatura if self.asignatura else None,
            nombre=nombre,
            creditos=creditos,
            curso=curso,
            cuatrimestre=cuatrimestre,
            grado_fk=grado_fk,
            obligatoria=obligatoria
        )

        self.service.validar_asignatura(asignatura)
        return asignatura
