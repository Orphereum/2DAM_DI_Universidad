import pytest
from unittest.mock import Mock
from app.service.proyecto_service import ProyectoService
from app.models.proyecto import Proyecto
from app.controller.proyectopage import ProyectoPage

# oara ejecutar todos los test a la vez 
#   pytest tests/test_proyecto.py -v (v para ver el nombre de cada tet y si pasa o da error)
# ejecutar UN test solo
    #pytest tests/test_proyecto.py::test_proyecto_model_valido -v

#TESTS SERVICIO 
def test_service_crud_completo(proyecto_service):
    """Verifica crear, actualizar y eliminar proyectos"""
    # Guardar
    proyecto_service.proyecto_repo.crear_proyecto = Mock(return_value=999)
    assert proyecto_service.crear_proyecto("Nuevo", "Desc", 1) == 999
    
    # Actualizar
    proyecto_service.actualizar_proyecto(1, "Actualizado", "Nueva Desc")
    proyecto_service.proyecto_repo.actualizar_proyecto.assert_called_once()
    
    # Eliminar
    proyecto_service.eliminar_proyecto(5)
    proyecto_service.proyecto_repo.eliminar_proyecto.assert_called_once_with(5)


def test_service_obtener_datos(proyecto_service):
    """Verifica que obtiene proyectos y subvenciones"""
    # Obtener por grupo
    proyecto_service.proyecto_repo.obtener_por_grupo = Mock(return_value=[(1, "P1", "D1")])
    assert len(proyecto_service.obtener_por_grupo(1)) == 1
    
    # Obtener completo (proyecto + subvenciones)
    proyecto_service.proyecto_repo.obtener_por_id = Mock(return_value=(1, "Test", "Desc"))
    proyecto_service.subvencion_repo.obtener_por_proyecto = Mock(return_value=[("Sub1", 1000)])
    
    proyecto, subvenciones = proyecto_service.obtener_proyecto_completo(1)
    assert proyecto is not None
    assert len(subvenciones) == 1


#TESTS VISTA

def test_page_crear_proyecto(proyecto_page):
    """Verifica creación de proyecto con datos válidos"""
    proyecto_page.ui.nombre_txt.text.return_value = "Proyecto Nuevo"
    proyecto_page.ui.descripcion_txt.toPlainText.return_value = "Descripción"
    proyecto_page.ui.comboBox_gruposInv.currentData.return_value = 1
    proyecto_page.proyecto_service.crear_proyecto.return_value = 123
    proyecto_page.actualizar_tabla_proyectos = Mock()
    proyecto_page.seleccionar_proyecto_por_id = Mock()
    proyecto_page.limpiar_campos = Mock()
    
    proyecto_page.crear_proyecto()
    
    proyecto_page.proyecto_service.crear_proyecto.assert_called_once()
    assert proyecto_page.nuevo_id == 123


def test_page_crear_validaciones(proyecto_page, mocker):
    """Verifica que no crea sin grupo o campos vacíos"""
    mock_msg = mocker.patch('PySide6.QtWidgets.QMessageBox')
    
    # Sin grupo
    proyecto_page.ui.comboBox_gruposInv.currentData.return_value = None
    proyecto_page.crear_proyecto()
    mock_msg.information.assert_called()
    
    # Campos vacíos
    proyecto_page.ui.comboBox_gruposInv.currentData.return_value = 1
    proyecto_page.ui.nombre_txt.text.return_value = ""
    proyecto_page.ui.descripcion_txt.toPlainText.return_value = ""
    proyecto_page.crear_proyecto()
    mock_msg.warning.assert_called()


def test_page_editar_y_eliminar(proyecto_page, mocker):
    """Verifica editar y eliminar proyectos"""
    # Editar
    proyecto_page.id_proyecto = 5
    proyecto_page.nombre_proyecto = "Viejo"
    proyecto_page.descrip_proyecto = "Vieja"
    proyecto_page.ui.nombre_txt.text.return_value = "Nuevo"
    proyecto_page.ui.descripcion_txt.toPlainText.return_value = "Nueva"
    proyecto_page.actualizar_tabla_proyectos = Mock()
    proyecto_page.limpiar_campos = Mock()
    
    proyecto_page.editar_proyecto()
    proyecto_page.proyecto_service.actualizar_proyecto.assert_called_once()
    
    # Eliminar
    proyecto_page.id_proyecto = 10
    mocker.patch('PySide6.QtWidgets.QMessageBox.question').return_value = 16384  # Yes
    proyecto_page.eliminar_proyecto()
    proyecto_page.proyecto_service.eliminar_proyecto.assert_called_once_with(10)


def test_page_seleccionar_y_limpiar(proyecto_page):
    """Verifica selección de proyecto y limpieza de campos"""
    # Seleccionar
    mock_item_id = Mock(text=Mock(return_value="42"))
    mock_item_nombre = Mock(text=Mock(return_value="Proyecto X"))
    mock_item_desc = Mock(text=Mock(return_value="Desc"))
    
    proyecto_page.tabla_proyectos.currentRow.return_value = 0
    proyecto_page.tabla_proyectos.item.side_effect = [mock_item_id, mock_item_nombre, mock_item_desc]
    proyecto_page.cargar_subvenciones_proyecto = Mock()
    
    proyecto_page.proyecto_seleccionado()
    
    assert proyecto_page.id_proyecto == 42
    proyecto_page.cargar_subvenciones_proyecto.assert_called_once_with(42)
    
    # Limpiar
    proyecto_page.limpiar_campos()
    proyecto_page.ui.nombre_txt.clear.assert_called()
    assert proyecto_page.id_proyecto is None


def test_page_filtrar_por_grupo(proyecto_page):
    """Verifica filtrado de proyectos por grupo"""
    proyecto_page.ui.comboBox_gruposInv.currentData.return_value = 3
    proyecto_page.proyecto_service.filtrar_por_grupo.return_value = [(1, "P1", "D1")]
    proyecto_page.generar_tabla = Mock()
    
    proyecto_page.filtrar_por_grupo()
    
    proyecto_page.proyecto_service.filtrar_por_grupo.assert_called_once_with(3)
    proyecto_page.generar_tabla.assert_called_once()
