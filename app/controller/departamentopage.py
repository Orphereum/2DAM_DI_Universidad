from PySide6.QtWidgets import QWidget, QTableWidgetItem
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
        self.ui.btnEliminar
    #editar
        self.ui.btnEditar
    #actualizar
        self.ui.btnActualizar
    #exportar PDF
        self.ui.btnInforme
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
        #Agarra el nombre del LineEdit y lo añade a la tabla departamentos
        #Agarra el combobox y lo añade a la tabla  facultades.
        nombre = self.ui.LineEditDepartamento.text()
        facultad = self.ui.comboBoxFacultad.currentText()
        
        fila = self.ui.tablaDepartamentos.rowsInserted(self, 0)
        #comprobacion que el nombre no este vacio
        if nombre:
            self.ui.tablaDepartamentos.setItem(fila, 0, QTableWidgetItem(nombre))
            self.ui.tablaFacultades.setItem(fila, 0, QTableWidgetItem(facultad))
            
        #por hacer.
        
        