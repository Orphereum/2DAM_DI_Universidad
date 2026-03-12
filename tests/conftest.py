import pytest
from unittest.mock import Mock
 
"""
Aqui debajo vuestros imports 🡫
"""
from app.service.proyecto_service import ProyectoService
from app.models.proyecto import Proyecto
from app.controller.proyectopage import ProyectoPage


@pytest.fixture
def proyecto_service(mocker):
    """Service de Proyecto con repositorios mockeados"""
    mock_proyecto_repo = Mock()
    mock_subvencion_repo = Mock()
    service = ProyectoService(mock_proyecto_repo, mock_subvencion_repo)
    mocker.patch('app.data.db.get_connection', return_value=Mock())
    return service


@pytest.fixture
def proyecto_valido():
    """Proyecto válido para tests"""
    return Proyecto(id_proyecto=None, nombre="Proyecto Test", descripcion="Descripción de prueba")


@pytest.fixture
def proyecto_existente():
    """Proyecto existente en BD"""
    return Proyecto(id_proyecto=1, nombre="Proyecto Existente", descripcion="Descripción existente")


@pytest.fixture
def proyecto_page(mocker):
    """Página de Proyecto con UI simulada"""
    page = ProyectoPage.__new__(ProyectoPage)  # Sin inicializar Qt
    page.ui = Mock()
    
    # Campos de formulario
    page.ui.nombre_txt = Mock(text=Mock(return_value=""), clear=Mock(), setText=Mock())
    page.ui.descripcion_txt = Mock(toPlainText=Mock(return_value=""), clear=Mock(), setPlainText=Mock())
    page.ui.comboBox_gruposInv = Mock(currentData=Mock(return_value=1), currentText=Mock(return_value="Grupo Test"))
    
    # Tablas
    page.tabla_proyectos = Mock()
    page.ui.tabla_proyectos = page.tabla_proyectos
    page.ui.tabla_subvenciones = Mock()
    
    # Botones
    page.ui.btn_editar = Mock()
    page.ui.btn_guardar = Mock()
    page.ui.btn_eliminar = Mock()
    page.ui.btn_limpiar = Mock()
    page.ui.btn_generarPDF_proyecto = Mock()
    page.ui.btn_generarPDF_todos = Mock()
    
    # Variables de instancia
    page.id_proyecto = None
    page.nuevo_id = None
    page.nombre_proyecto = ""
    page.descrip_proyecto = ""
    page.proyecto_service = Mock()
    
    return page
