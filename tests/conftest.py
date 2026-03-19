import pytest
from unittest.mock import Mock
from app.service.grado_service import GradoService
from app.models.grado import Grado
from app.controller.gradopage import GradoPage  
"""
Aqui debajo vuestros imports 🡫
"""
from app.service.proyecto_service import ProyectoService
from app.models.proyecto import Proyecto
from app.controller.proyectopage import ProyectoPage

@pytest.fixture
def grado_service(mocker):
    service = GradoService()
    mocker.patch('app.data.db.get_connection', return_value=Mock())
    return service

@pytest.fixture
def grado_valido():
    return Grado(id_grado=None, nombre="Ingeniería", codigo="ING_TEST", 
                 duracion_anios=4, creditos_totales=240, tipo="Grado", 
                 estado=True, id_facultad=1)

@pytest.fixture
def grado_existente():
    return Grado(id_grado=1, nombre="Existente", codigo="EXIST999", 
                 duracion_anios=4, creditos_totales=240, tipo="Grado", 
                 estado=True, id_facultad=1)

@pytest.fixture
def grado_page(mocker):
    page = GradoPage()  
    page.service = Mock()
    page.ui = Mock()
    page.ui.tbl_grados = Mock()
    page.ui.txt_nombre = Mock(text=Mock(return_value=""), clear=Mock())
    page.ui.txt_codigo = Mock(text=Mock(return_value=""), clear=Mock())
    page.ui.sp_duracion = Mock(value=Mock(return_value=0), setValue=Mock())
    page.ui.sp_creditos = Mock(value=Mock(return_value=0), setValue=Mock())
    page.ui.cb_tipo = Mock(currentText=Mock(return_value=""), setCurrentText=Mock(), setCurrentIndex=Mock())
    page.ui.chk_activo = Mock(isChecked=Mock(return_value=False))
    page.ui.grp_formulario = Mock(setEnabled=Mock())
    page.ui.cb_facultad = Mock(currentData=Mock(return_value=1))
    return page

"""
Aqui debajo vuestros FIXTURE 🡫
"""
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
