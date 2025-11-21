from app.controller.homewindow import HomeWindow


class AppController:
    """Controlador principal de la aplicación."""
    def __init__(self):

        self.home = HomeWindow()

        self.pages = {}

        self._setup_pages()

        self.setup_connections()

        self.home.show()

    def _setup_pages(self):
        #creamos las paginas y las añadimos al contenedor stacked widget
        
        #pagina1 = Pagina1(self.home) => la pagina sera del primero que cree la ventana de su entidad
      
        #self.pages["pagina1"] = pagina1

        #añadimos al stacked widget cada widget de la ventana personal de cada quien
        stacked = self.home.ui.stackedWidget
        #stacked.addWidget(pagina1)

        #ponemos que se muestre al iniciar la primera pagina
        
        #stacked.setCurrentWidget(pagina1)

    #generando la conexion de los botones con cada pagina
    def setup_connections(self):
        self.home.ui.btnPage1.clicked.connect(self.go_to_pagina(Pagina1))
       

    #funcion generica para ir a cada pagina
    def go_to_pagina(self, var):
        self.show_page(var)

    #mostramos la ventana
    def show_page(self, name: str):
        widget = self.pages[name]
        self.home.ui.stackedWidget.setCurrentWidget(widget)
