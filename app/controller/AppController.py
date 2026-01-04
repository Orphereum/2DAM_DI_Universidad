from app.controller.homewindow import HomeWindow
from app.controller.universidadpage import UniversidadPage
from app.controller.profesorpage import ProfesorPage
from app.controller.departamentopage import DepartamentoPage
from app.controller.gradopage import GradoPage


class AppController:
    """Controlador principal de la aplicación."""
    def __init__(self):
        self.home = HomeWindow()
        self.pages = {}

        self._setup_pages()
        self.setup_connections()

        self.home.show()

    def _setup_pages(self):
        stacked = self.home.ui.stackedWidget

        universidad = UniversidadPage(stacked)
        profesor = ProfesorPage(stacked)
        departamento = DepartamentoPage(stacked)
        grado = GradoPage(stacked)

        self.pages["universidad"] = universidad
        self.pages["profesor"] = profesor
        self.pages["departamento"] = departamento
        self.pages["grado"] = grado

        stacked.addWidget(universidad)
        stacked.addWidget(profesor)
        stacked.addWidget(departamento)
        stacked.addWidget(grado)   

        stacked.setCurrentWidget(universidad)

    def setup_connections(self):
        self.home.ui.btnUniversidad.clicked.connect(self.go_to_universidadPage)
        self.home.ui.btnProfesor.clicked.connect(self.go_to_profesor)
        self.home.ui.btnDepartamento.clicked.connect(self.go_to_departamento)
        self.home.ui.btnGrado.clicked.connect(self.go_to_grado)

    def go_to_universidadPage(self):
        self.show_page("universidad")

    def go_to_profesor(self):
        self.show_page("profesor")

    def go_to_departamento(self):
        self.show_page("departamento")

    def go_to_grado(self):
        self.show_page("grado")

    def show_page(self, name: str):
        widget = self.pages[name]
        self.home.ui.stackedWidget.setCurrentWidget(widget)
