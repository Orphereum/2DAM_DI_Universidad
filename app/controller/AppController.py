from app.controller.homewindow import HomeWindow
from app.controller.Pagina1 import Pagina1


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
        pagina1 = Pagina1(self.home)

        self.pages["pagina1"] = pagina1

        stacked = self.home.ui.stackedWidget
        stacked.addWidget(pagina1)

        #ponemos que se muestre al iniciar la primera pagina
        stacked.setCurrentWidget(pagina1)

    #generando la conexion de los botones con cada pagina
    def setup_connections(self):
        self.home.ui.btnPage1.clicked.connect(self.go_to_pagina1)

    #funcion generica para ir a cada pagina
    def go_to_pagina1(self):
        self.show_page("pagina1")

    #mostramos la ventana
    def show_page(self, name: str):
        widget = self.pages[name]
        self.home.ui.stackedWidget.setCurrentWidget(widget)
