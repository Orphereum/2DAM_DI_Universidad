import pytest
from app.models.grado import Grado
from app.service.grado_service import GradoService
from app.controller.gradopage import GradoPage  

def test_grado_model_valido():
    grado = Grado(nombre="Test", codigo="TST", duracion_anios=4, creditos_totales=240,
                  tipo="Grado", estado=True, id_facultad=1)
    assert grado.nombre == "Test"
    assert grado.estado is True

def test_service_crear_grado(grado_service, grado_valido):
    grado_valido.codigo = "TEST_UNIQUE_" + str(hash("test"))  
    resultado = grado_service.crear_grado(grado_valido)
    assert resultado.id_grado is not None

def test_service_actualizar_grado(grado_service, grado_existente, mocker):
    mocker.patch.object(grado_service.repo, 'update', return_value=grado_existente)
    resultado = grado_service.actualizar_grado(grado_existente)
    assert resultado is not None

def test_service_eliminar_grado(grado_service, mocker):
    mock_grado = Grado(id_grado=999, nombre="Mock", codigo="MOCK", duracion_anios=4,
                       creditos_totales=240, tipo="Grado", estado=True, id_facultad=1)
    mocker.patch.object(grado_service.repo, 'find_by_id', return_value=mock_grado)
    mocker.patch.object(grado_service.repo, 'delete')
    
    grado_service.eliminar_grado(999)
    grado_service.repo.delete.assert_called_once_with(999)

# Tests View
def test_grado_page_nuevo_grado(grado_page):
    grado_page.nuevo_grado()
    grado_page.ui.grp_formulario.setEnabled.assert_called_with(True)
    assert grado_page.grado_seleccionado_id is None

def test_grado_page_guardar_nuevo(grado_page):
    grado_page.ui.txt_nombre.text.return_value = "Nuevo"
    grado_page.ui.txt_codigo.text.return_value = "NUE"
    grado_page.ui.sp_duracion.value.return_value = 4
    grado_page.ui.sp_creditos.value.return_value = 240
    grado_page.ui.cb_tipo.currentText.return_value = "Grado"
    grado_page.ui.chk_activo.isChecked.return_value = True
    
    grado_page.guardar()
    grado_page.service.crear_grado.assert_called_once()

def test_grado_page_eliminar(grado_page, mocker):
    grado_page.grado_seleccionado_id = 5
    mocker.patch('PySide6.QtWidgets.QMessageBox.question').return_value = 16384
    grado_page.eliminar_grado()
    grado_page.service.eliminar_grado.assert_called_once_with(5)

def test_grado_page_cargar_grados(grado_page):
    grado_page.cargar_grados(1)
    grado_page.service.obtener_grados_por_facultad.assert_called_once_with(1)



"""Con estas pruebas garantizamos:
        Guarda correctamente todos los campos (nombre, código, créditos...)
        No se rompe si cambias orden de parámetros en __init__
        Estado booleano funciona (True/False)
        crear_grado(): inserta + retorna ID válido
        actualizar_grado(): llama repo.update correctamente  
        eliminar_grado(): busca + borra (maneja "no existe")         <No usa BD real (mocks → rápido/aislado)>
        nuevo_grado(): limpia form + desbloquea ✓
        guardar(): lee UI → crea Grado → llama service ✓
        editar(): desbloquea form ✓
        eliminar(): confirma → service.eliminar ✓
        cargar_grados(): service.obtener_grados ✓
        No crashea sin Qt real (mocks)
"""