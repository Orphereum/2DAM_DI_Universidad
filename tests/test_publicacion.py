from unittest.mock import Mock

import pytest

from app.controller.publicacionpage import PublicacionPage
from app.models.publicacion import Publicacion
from app.service.publicacion_service import PublicacionService


def test_publicacion_model_valido():
    publicacion = Publicacion(
        id_publicacion=None,
        titulo="Titulo de prueba",
        descripcion="Descripcion",
        fecha_publicacion="2026-05-22",
        tipo="Articulo",
        id_grupoDebate=1
    )

    assert publicacion.titulo == "Titulo de prueba"
    assert publicacion.id_grupoDebate == 1


def test_service_crear_publicacion_valida():
    repo = Mock()
    repo.existe_grupo_debate.return_value = True
    repo.crear_publicacion.return_value = 10
    service = PublicacionService(repo)

    resultado = service.crear_publicacion(
        " Titulo ",
        " Descripcion ",
        "2026-05-22",
        " Articulo ",
        1
    )

    assert resultado == 10
    repo.crear_publicacion.assert_called_once_with(
        "Titulo",
        "Descripcion",
        "2026-05-22",
        "Articulo",
        1
    )


def test_service_valida_titulo_fecha_y_grupo():
    repo = Mock()
    repo.existe_grupo_debate.return_value = False
    service = PublicacionService(repo)

    with pytest.raises(ValueError, match="titulo"):
        service.crear_publicacion("", "Desc", "2026-05-22", "Articulo")

    with pytest.raises(ValueError, match="fecha"):
        service.crear_publicacion("Titulo", "Desc", "22/05/2026", "Articulo")

    with pytest.raises(ValueError, match="grupo"):
        service.crear_publicacion("Titulo", "Desc", "2026-05-22", "Articulo", 99)


def test_service_actualizar_y_eliminar():
    repo = Mock()
    repo.existe_grupo_debate.return_value = True
    service = PublicacionService(repo)

    service.actualizar_publicacion(
        5,
        "Nuevo titulo",
        "Nueva descripcion",
        "2026-05-22",
        "Noticia",
        1
    )
    repo.actualizar_publicacion.assert_called_once()

    service.eliminar_publicacion(5)
    repo.eliminar_publicacion.assert_called_once_with(5)


def test_page_crear_publicacion(mocker):
    page = PublicacionPage.__new__(PublicacionPage)
    page.publicacion_service = Mock()
    page._leer_formulario = Mock(
        return_value=("Titulo", "Desc", "2026-05-22", "Articulo", None)
    )
    page.cargar_tabla = Mock()
    page.limpiar_campos = Mock()
    mocker.patch("app.controller.publicacionpage.QMessageBox")

    page.crear_publicacion()

    page.publicacion_service.crear_publicacion.assert_called_once_with(
        "Titulo",
        "Desc",
        "2026-05-22",
        "Articulo",
        None
    )
    page.cargar_tabla.assert_called_once()
    page.limpiar_campos.assert_called_once()


def test_page_editar_y_eliminar_publicacion(mocker):
    page = PublicacionPage.__new__(PublicacionPage)
    page.id_publicacion = 7
    page.publicacion_service = Mock()
    page._leer_formulario = Mock(
        return_value=("Titulo", "Desc", "2026-05-22", "Articulo", None)
    )
    page.cargar_tabla = Mock()
    page.limpiar_campos = Mock()
    mock_msg = mocker.patch("app.controller.publicacionpage.QMessageBox")
    mock_msg.question.return_value = mock_msg.Yes

    page.editar_publicacion()
    page.publicacion_service.actualizar_publicacion.assert_called_once_with(
        7,
        "Titulo",
        "Desc",
        "2026-05-22",
        "Articulo",
        None
    )

    page.eliminar_publicacion()
    page.publicacion_service.eliminar_publicacion.assert_called_once_with(7)
