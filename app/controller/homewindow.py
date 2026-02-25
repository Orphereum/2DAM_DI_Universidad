from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtGui import QIcon
from app.view.HomeWindow_ui import Ui_HomeWindow
import os
import sys

def resource_path(relative_path):
    """Para PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        
        # TÍTULO E ICONO (nuevo)
        self.setWindowTitle("Gestor Universidad")
        self.setWindowIcon(QIcon(resource_path("universidad.ico")))
        
        w = self.ui.stackedWidget
        w.setMinimumSize(881, 621)
        w.setMaximumSize(881, 621)

        self.load_styles()
        self.fix_margins()

    def load_styles(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        style_path = os.path.join(base_dir, "styles", "app_style.qss")

        print("Intentando cargar estilos desde:", style_path) 

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                style = f.read()
                self.setStyleSheet(style)
                print(" Estilos cargados correctamente")
        except FileNotFoundError:
            print("Archivo de estilos NO encontrado:", style_path)
        except Exception as e:
            print("Error cargando estilos:", e)
        
    def fix_margins(self):
       self.setContentsMargins(0, 0, 0, 0)

       self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
       self.ui.scrollArea.setContentsMargins(0, 0, 0, 0)
       self.ui.scrollArea.setViewportMargins(0, 0, 0, 0)

       main_layout = self.ui.centralwidget.layout()
       if main_layout:
            main_layout.setContentsMargins(0, 0, 0, 0)
            main_layout.setSpacing(0)

       menu_layout = self.ui.menuWidget.layout()
       if menu_layout:
            menu_layout.setContentsMargins(0, 0, 0, 0)
            menu_layout.setSpacing(8) 

       self.ui.stackedWidget.setContentsMargins(0, 0, 0, 0)
       for i in range(self.ui.stackedWidget.count()):
            page = self.ui.stackedWidget.widget(i)
            layout = page.layout()
            if layout:
                layout.setContentsMargins(0, 0, 0, 0)

       if hasattr(self.ui, "statusbar"):
            self.ui.statusbar.hide()
