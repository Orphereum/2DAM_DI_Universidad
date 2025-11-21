from app.controller.homewindow import HomeWindow
from app.controller.universidadpage import UniversidadPage
from app.controller.profesorpage import ProfesorPage


class AppController:
    """Controlador principal de la aplicación."""
    def __init__(self):

        self.home = HomeWindow()

        self.pages = {}#actua como un siccionario de paginas

        self._setup_pages() #las añadimos al stackerdwidget

   #la funcion de los botones
        self.setup_connections()

        self.home.show()

    def _setup_pages(self):
        #creamos las paginas y las añadimos al contenedor stacked widget
        universidad = UniversidadPage(self.home)
        profesor = ProfesorPage(self.home)


        self.pages["universidad"] = universidad
        self.pages["profesor"] = profesor

        stacked = self.home.ui.stackedWidget
        stacked.addWidget(universidad)
        stacked.addWidget(profesor)

        #ponemos que se muestre al iniciar la primera pagina
        stacked.setCurrentWidget(universidad)

    #generando la conexion de los botones con cada pagina
    def setup_connections(self):
        self.home.ui.btnUniversidad.clicked.connect(self.go_to_universidadPage)
        self.home.ui.btnProfesor.clicked.connect(self.go_to_profesor)

    #funcion generica para ir a cada pagina
    def go_to_universidadPage(self):
        self.show_page("universidad")

    def go_to_profesor(self):
        self.show_page("profesor")

    #mostramos la ventana
    def show_page(self, name: str):
        widget = self.pages[name]
        self.home.ui.stackedWidget.setCurrentWidget(widget)
