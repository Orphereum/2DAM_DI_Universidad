from app.controller.homewindow import HomeWindow
from app.controller.universidadpage import UniversidadPage
from app.controller.profesorpage import ProfesorPage
from app.controller.departamentopage import DepartamentoPage
from app.controller.gradopage import GradoPage
from app.controller.asignaturapage import AsignaturaPage
from app.controller.clasepage import ClasePage
from app.repository.asignatura_repo import AsignaturaRepository
from app.repository.grado_repo import GradoRepository
from app.repository.clase_repo import ClaseRepository
from app.repository.edificio_repo import EdificioRepository
from app.service.asignatura_service import AsignaturaService
from app.service.clase_service import ClaseService
from app.controller.edificiopage import EdificioPage
from app.repository.edificio_repo import EdificioRepository
from app.repository.facultad_repo import FacultadRepo
from app.service.edificio_service import EdificioService
from app.controller.proyectopage import ProyectoPage
from app.repository.proyecto_repo import ProyectoRepository
from app.service.proyecto_service import ProyectoService
from app.repository.grupoInv_repo import GrupoInvRepository
from app.service.grupoInv_service import GrupoInvService 



from app.data.db import get_connection   
class AppController:
    """Controlador principal de la aplicación."""

    def __init__(self):
        self.home = HomeWindow()
        self.pages = {}
        self._test_db() # PRUEBA
        self._setup_pages()
        self._setup_connections()

        self.home.show()
        
    def _test_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) as total FROM universidad;")
        total = cursor.fetchone()["total"]

        print("================================")
        print("Total universidades en BD:", total)
        print("================================")

        conn.close()
    # -------------------------
    # CREACIÓN DE PÁGINAS
    # -------------------------
    def _setup_pages(self):
        stacked = self.home.ui.stackedWidget

        # PÁGINAS SIN SERVICE
        universidad = UniversidadPage(stacked)
        profesor = ProfesorPage(stacked)
        departamento = DepartamentoPage(stacked)
        grado = GradoPage(stacked)

        # -------------------------
        # DEPENDENCIAS ASIGNATURA
        # -------------------------

        asignatura_repo = AsignaturaRepository()
        grado_repo = GradoRepository()

        asignatura_service = AsignaturaService(
            asignatura_repo,
            grado_repo
        )

        asignatura = AsignaturaPage(asignatura_service, stacked)

        # -------------------------
        # DEPENDENCIAS CLASE
        # -------------------------

        clase_repo = ClaseRepository()
        edificio_repo = EdificioRepository()

        clase_service = ClaseService(
            clase_repo,
            edificio_repo
        )

        clase = ClasePage(clase_service, stacked)
        
        
        # -------------------------
        # DEPENDENCIAS EDIFICIO
        # -------------------------
        edificio_repo = EdificioRepository()
        facultad_repo = FacultadRepo()

        edificio_service = EdificioService(
            edificio_repo,
            facultad_repo
        )

        edificio = EdificioPage(edificio_service, stacked)
        
        # -------------------------
        # DEPENDENCIAS GRUPO INVESTIGACIÓN
        # -------------------------
        grupoInv_repo = GrupoInvRepository()

        grupoInv_service = GrupoInvService(
            grupoInv_repo
        )

        #grupoInv = GrupoInvPage(grupoInv_service, stacked)
        
        # -------------------------
        # DEPENDENCIAS PROYECTO
        # -------------------------
        proyecto_repo = ProyectoRepository()

        proyecto_service = ProyectoService(
            proyecto_repo
        )

        proyecto = ProyectoPage(proyecto_service, grupoInv_service, stacked)
            
        

        # REGISTRO DE PÁGINAS
        self.pages = {
            "universidad": universidad,
            "profesor": profesor,
            "departamento": departamento,
            "grado": grado,
            "asignatura": asignatura,
            "clase": clase,
            "edificio": edificio,
            "proyecto": proyecto
        }

        # AÑADIR AL STACK
        for page in self.pages.values():
            stacked.addWidget(page)

        # PÁGINA INICIAL
        stacked.setCurrentWidget(universidad)


    # -------------------------
    # CONEXIONES DE MENÚ
    # -------------------------
    def _setup_connections(self):
        self.home.ui.btnUniversidad.clicked.connect(
            lambda: self.show_page("universidad")
        )
        self.home.ui.btnProfesor.clicked.connect(
            lambda: self.show_page("profesor")
        )
        self.home.ui.btnDepartamento.clicked.connect(
            lambda: self.show_page("departamento")
        )
        self.home.ui.btnGrado.clicked.connect(
            lambda: self.show_page("grado")
        )
        self.home.ui.btnAsignatura.clicked.connect(
            lambda: self.show_page("asignatura")
        )
        self.home.ui.btnClase.clicked.connect(
            lambda: self.show_page("clase")
        )
        self.home.ui.btnEdificio.clicked.connect(
            lambda: self.show_page("edificio")
        )
        self.home.ui.btnProyecto.clicked.connect(
            lambda: self.show_page("proyecto")
        )

    # -------------------------
    # CAMBIO DE PÁGINA
    # -------------------------
    def show_page(self, name: str):
        widget = self.pages.get(name)
        if widget:
            self.home.ui.stackedWidget.setCurrentWidget(widget)