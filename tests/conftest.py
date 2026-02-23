import pytest
from unittest.mock import Mock
from app.service.grado_service import GradoService
from app.models.grado import Grado
from app.controller.gradopage import GradoPage  
"""
Aqui debajo vuestros imports 🡫
"""


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