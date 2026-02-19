import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.controller.AppController import AppController
import app.resources.resources_rc

# FIX DPI + ESCALADO WINDOWS (ANTES de QApplication)
if os.name == 'nt':  # Solo Windows
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    os.environ["QT_SCALE_FACTOR_ROUNDING_POLICY"] = "PassThrough"

# Crear QApplication con DPI policy
app = QApplication(sys.argv)
app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
app.setApplicationName("Gestor Universidad")

# Cargar estilos dinámicos (funciona en dev + EXE)
def load_styles():
    if getattr(sys, 'frozen', False):
        qss_path = os.path.join(sys._MEIPASS, 'app', 'styles', 'app_style.qss')
    else:
        qss_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'app', 'styles', 'app_style.qss')
    
    try:
        with open(qss_path, 'r', encoding='utf-8') as f:
            app.setStyleSheet(f.read())
        print(" Estilos cargados desde:", qss_path)
    except FileNotFoundError:
        print(" QSS no encontrada, usando default")

load_styles()

controller = AppController()

sys.exit(app.exec())
