from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from app.view.DepartamentoPage_ui import Ui_DepartamentoPage

class DepartamentoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DepartamentoPage()
        self.ui.setupUi(self)


    #función de los botones

    #agregar
        self.ui.btnAgregar.clicked.connect(self.Agregar)
    #eliminar
        self.ui.btnEliminar.clicked.connect(self.Eliminar)
    #editar
        self.ui.btnEditar.clicked.connect(self.Editar)
    #actualizar
        self.ui.btnActualizar.clicked.connect(self.Actualizar)
    #exportar PDF
        self.ui.btnInforme.clicked.connect(self.ExportarPDF)
    #line edit text nombre departamento
        self.ui.LineEditDepartamento
    #comboBox facultad
        self.ui.comboBoxFacultad
    #ventana izquierda
        self.ui.tablaFacultades
    #ventana derecha
        self.ui.tablaDepartamentos


    #metodos
    def Agregar(self):
        """Inserta un nuevo departamento con los datos del formulario."""
        nombre     = self.ui.LineEditDepartamento.text().strip()
        id_facultad = self.ui.comboBoxFacultad.currentData()
 
        try:
            self._service.agregar(nombre, id_facultad)
            self._cargar_departamentos(self._id_fac_sel)
            self.ui.LineEditDepartamento.clear()
            QMessageBox.information(self, "Éxito", "Departamento añadido correctamente")
        except ValueError as e:
            QMessageBox.warning(self, "Atención", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo añadir el departamento:\n{e}")
        
    def Eliminar(self):
        """Elimina el departamento seleccionado en la tabla derecha."""
        indices = self.ui.tablaDepartamentos.selectionModel().selectedRows()
        if not indices:
            QMessageBox.warning(self, "Atención", "Selecciona un departamento para eliminar")
            return
 
        fila       = indices[0].row()
        id_item    = self._modelo_dpts.item(fila, 0)
        nombre_item = self._modelo_dpts.item(fila, 1)
 
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Eliminar el departamento «{nombre_item.text()}»?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta != QMessageBox.StandardButton.Yes:
            return
 
        try:
            self._service.eliminar(int(id_item.text()))
            self._cargar_departamentos(self._id_fac_sel)
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Departamento eliminado")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar:\n{e}")
 

    def Editar(self):
       
        indices = self.ui.tablaDepartamentos.selectionModel().selectedRows()
        if not indices:
            QMessageBox.warning(self, "Atención", "Selecciona un departamento para editar")
            return
 
        fila          = indices[0].row()
        id_item       = self._modelo_dpts.item(fila, 0)
        nombre_item   = self._modelo_dpts.item(fila, 1)
        facultad_item = self._modelo_dpts.item(fila, 2)
 
        # Guardar ID en edición y rellenar formulario
        self._id_editando = int(id_item.text())
        self.ui.LineEditDepartamento.setText(nombre_item.text())
 
        # Seleccionar la facultad correspondiente en el combo
        idx = self.ui.comboBoxFacultad.findText(facultad_item.text())
        self.ui.comboBoxFacultad.setCurrentIndex(idx if idx != -1 else 0)
 
        self.ui.btnActualizar.setEnabled(True)
        self.ui.btnAgregar.setEnabled(False)
    
    def Actualizar(self):
        
        if self._id_editando is None:
            QMessageBox.warning(self, "Atención", "Primero selecciona un departamento y pulsa Editar")
            return
 
        nombre      = self.ui.LineEditDepartamento.text().strip()
        id_facultad = self.ui.comboBoxFacultad.currentData()
 
        try:
            self._service.editar(self._id_editando, nombre, id_facultad)
            self._cargar_departamentos(self._id_fac_sel)
            self._limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Departamento actualizado correctamente")
        except ValueError as e:
            QMessageBox.warning(self, "Atención", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar:\n{e}")
            
    def ExportarPDF(self):
        from PySide6.QtWidgets import QFileDialog
        from departamento_report import generar_informe_departamentos 

        ruta_archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Informe de Departamentos",
            "informe_departamentos.pdf",
            "Archivos PDF (*.pdf)"
        )

        if not ruta_archivo:
            return

        try:
            departamentos = self._service.listar_todos()
            
            facultades_dict = {}
            for i in range(self.ui.comboBoxFacultad.count()):
                id_facultad = self.ui.comboBoxFacultad.itemData(i)
                nombre_facultad = self.ui.comboBoxFacultad.itemText(i)
                if id_facultad is not None:
                    facultades_dict[id_facultad] = nombre_facultad

            generar_informe_departamentos(departamentos, facultades_dict, ruta_archivo)
            
            QMessageBox.information(self, "Éxito", f"Informe generado en:\n{ruta_archivo}")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo generar el informe:\n{str(e)}")